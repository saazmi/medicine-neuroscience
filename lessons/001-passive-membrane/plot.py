"""Original synthetic passive-membrane plots; all calculations use SI units.

Model reference: Gerstner et al., Neuronal Dynamics, section 1.3.
These are analytical predictions, not patient data or neuronal recordings.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
REST = -70e-3
CURRENT = 50e-12
TIME = np.linspace(0, 0.08, 801)

def response(time, resistance, capacitance):
    return REST + CURRENT * resistance * (1 - np.exp(-time / (resistance * capacitance)))

def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False})
    fig, axes = plt.subplots(1, 2, figsize=(13, 6.2), sharey=True)
    colors = ["#087e8b", "#5243aa", "#c15821"]
    for c_pf, col in zip([50, 100, 200], colors):
        axes[0].plot(TIME*1e3, response(TIME, 100e6, c_pf*1e-12)*1e3,
                     label=f"C = {c_pf} pF; τ = {c_pf/10:g} ms", color=col, lw=2.6)
    for r_mohm, col in zip([50, 100, 200], colors):
        axes[1].plot(TIME*1e3, response(TIME, r_mohm*1e6, 100e-12)*1e3,
                     label=f"R = {r_mohm} MΩ; τ = {r_mohm/10:g} ms", color=col, lw=2.6)
    axes[0].set_title("A · Change capacitance / Varier la capacité\nR = 100 MΩ", pad=15)
    axes[1].set_title("B · Change resistance / Varier la résistance\nC = 100 pF", pad=15)
    axes[0].set_ylabel("Membrane potential / Potentiel de membrane (mV)")
    for ax in axes:
        ax.set_xlabel("Time / Temps (ms)")
        ax.set_xlim(0, 80)
        ax.set_ylim(-70.5, -59)
        ax.grid(alpha=.18)
        ax.legend(loc="lower right", frameon=False, fontsize=10)
    fig.suptitle("ONE MODEL, TWO QUESTIONS / UN MODÈLE, DEUX QUESTIONS", x=.075,
                 ha="left", fontsize=17, fontweight="bold", y=.98)
    fig.text(.075,.895,"Synthetic current step / Échelon simulé : +50 pA at / à t = 0; Eₗ = −70 mV",
             fontsize=11, color="#475569")
    fig.text(.075,.075,"A: same final change, different speed.\nMême variation finale, vitesse différente.", fontsize=10)
    fig.text(.55,.075,"B: final change and time constant both change.\nVariation finale et constante de temps modifiées.", fontsize=10)
    fig.text(.075,.012,"Passive, uniform, constant-parameter model; no action potentials. / Modèle passif uniforme, sans potentiel d'action.",
             fontsize=9, color="#475569")
    fig.subplots_adjust(left=.075,right=.98,bottom=.22,top=.77,wspace=.14)
    fig.savefig(OUT / "response.png", dpi=150, facecolor="white")
    fig.savefig(OUT / "response.svg", facecolor="white")
    # Concrete checks of the worked numerical example and graph boundaries.
    assert np.isclose(response(np.array([0.]), 100e6, 100e-12)[0], REST)
    assert np.isclose(response(np.array([.01]), 100e6, 100e-12)[0], -.06683939720585721)
    assert np.isclose(response(np.array([10.]), 100e6, 100e-12)[0], -.065)
    print("Figure regenerated; initial value, worked example, and asymptote verified.")

if __name__ == "__main__":
    main()
