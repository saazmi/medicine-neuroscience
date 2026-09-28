"""Vérifie et synchronise la couverture du programme par rapport aux 367 items du R2C.

Usage :
    python tools/r2c.py          # vérifier (code de sortie 1 en cas d'incohérence)
    python tools/r2c.py sync     # régénérer les listes d'items dans programme/*.md

Sources de vérité : curriculum/modules.csv (modules) et curriculum/r2c-items.csv
(item -> module principal, modules associés, fichier de contenu rédigé).
Bibliothèque standard uniquement.
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "curriculum" / "modules.csv"
ITEMS = ROOT / "curriculum" / "r2c-items.csv"
START, END = "<!-- r2c:debut -->", "<!-- r2c:fin -->"
BLOCK = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def render(module_id, primary, shared, titles):
    lines = [START, "", "*Liste générée par `python tools/r2c.py sync` — ne pas modifier à la main.*", ""]
    if primary:
        lines.append(f"**Items principaux ({len(primary)}) :**")
        lines.append("")
        lines += [f"- **{i['item']}** — {i['intitule']}" for i in primary]
        lines.append("")
    if shared:
        lines.append(f"**Items partagés ({len(shared)}), traités principalement ailleurs :**")
        lines.append("")
        lines += [f"- {i['item']} — {i['intitule']} *(principal : {i['module']} {titles[i['module']]})*"
                  for i in shared]
        lines.append("")
    if not primary and not shared:
        lines += ["Aucun item du R2C n'est rattaché directement à ce module : il fournit les bases "
                  "que les items présupposent.", ""]
    lines.append(END)
    return "\n".join(lines)


def main(argv):
    sync = argv[1:] == ["sync"]
    errors = []
    modules = {m["id"]: m for m in read_csv(MODULES)}
    titles = {k: m["titre"] for k, m in modules.items()}
    items = read_csv(ITEMS)

    numbers = [int(i["item"]) for i in items]
    if numbers != list(range(1, 368)):
        errors.append("r2c-items.csv doit contenir les items 1 à 367, dans l'ordre.")

    primary, shared = defaultdict(list), defaultdict(list)
    for i in items:
        if i["module"] not in modules:
            errors.append(f"Item {i['item']} : module inconnu {i['module']!r}.")
        primary[i["module"]].append(i)
        for other in filter(None, i["modules_associes"].split(";")):
            if other not in modules:
                errors.append(f"Item {i['item']} : module associé inconnu {other!r}.")
            shared[other].append(i)
        if i["contenu"] and not (ROOT / i["contenu"]).exists():
            errors.append(f"Item {i['item']} : fichier de contenu introuvable {i['contenu']}.")

    for mid, m in modules.items():
        path = ROOT / m["fichier"]
        if not path.exists():
            errors.append(f"{mid} : fichier manquant {m['fichier']}.")
            continue
        text = path.read_text(encoding="utf-8")
        if not BLOCK.search(text):
            errors.append(f"{mid} : marqueurs {START} … {END} absents.")
            continue
        expected = render(mid, primary[mid], shared[mid], titles)
        new = BLOCK.sub(lambda _: expected, text)
        if new != text:
            if sync:
                path.write_text(new, encoding="utf-8", newline="\n")
                print(f"synchronisé : {m['fichier']}")
            else:
                errors.append(f"{mid} : liste d'items non synchronisée (lancer `python tools/r2c.py sync`).")

    written = sum(1 for i in items if i["contenu"])
    print(f"Modules : {len(modules)} · items R2C : {len(items)} · "
          f"items avec contenu rédigé : {written}/{len(items)} ({100 * written / len(items):.1f} %)")
    by_phase = defaultdict(int)
    for m in modules.values():
        by_phase[m["phase"]] += 1
    print("Modules par phase : " + ", ".join(f"{p}={n}" for p, n in sorted(by_phase.items())))
    for e in errors:
        print("ERREUR : " + e, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
