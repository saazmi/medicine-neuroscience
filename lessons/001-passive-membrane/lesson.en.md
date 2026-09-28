# 001 — A passive membrane: from biology to an equation

*Version française (référence) : [lesson.md](lesson.md).*

Status: source_checked; not independently expert-reviewed. Prerequisites: membrane/ion basics, current and voltage, first-order ODEs. This is a teaching-style demonstration, not the beginning of the entire curriculum.

**Objectives:** define the variables; check units; derive a step response; distinguish response amplitude from response speed; explain limitations.

In an electrical approximation, a membrane separates charge while ion channels provide conductive pathways. We represent a spatially uniform, passive cell by a capacitance and a leak conductance. This approximation does not reproduce active spike generation. [S1, S2]

![Synthetic membrane responses, bilingual axes](response.png)

The curves are calculated examples, not recordings. Panels change one parameter at a time. Values are chosen for teaching, not asserted as universal neuronal constants.

For inward injected current defined as positive:

$$C_m\frac{dV}{dt}=I_{\mathrm{inj}}-g_L(V-E_L).$$

| Symbol | Meaning | SI unit |
|---|---|---|
| $V$ | Inside-minus-outside membrane voltage | V |
| $C_m$ | Whole-cell capacitance | F |
| $g_L$ | Total passive leak conductance | S |
| $E_L$ | Effective leak reversal potential; resting voltage in this model without injected current | V |
| $I_{\mathrm{inj}}$ | Injected current, positive inward | A |

These are whole-cell quantities, not quantities per unit area. Keep conventions consistent. The current balance and leak term follow S1–S2.

For constant $I_0$, $V(0)=E_L$, and $R_m=1/g_L$:

$$V(t)=E_L+I_0R_m(1-e^{-t/\tau_m}),\qquad \tau_m=R_mC_m.$$

An original worked example: set $E_L=-70$ mV, $I_0=50$ pA, $R_m=100$ MΩ, $C_m=100$ pF.

$$I_0R_m=(50\times10^{-12})(100\times10^6)=0.005\ \mathrm{V}.$$

$$\tau_m=(100\times10^6)(100\times10^{-12})=0.01\ \mathrm{s}.$$

Thus $V_\infty=-65$ mV and $V(10\,\mathrm{ms})\approx-66.84$ mV. Verify by substitution; do not memorize the numbers.

**Mathematical extension:** let $x=V-E_L$. The equation becomes $C_m\dot{x}+g_Lx=I$. For a sinusoidal input, solving this linear ODE gives impedance

$$Z(\omega)=\frac{1}{g_L+i\omega C_m}.$$

Its units are ohms. Derive the magnitude and phase yourself; explain what they predict before writing code.

**Biological boundary:** constant conductance omits voltage-dependent channel dynamics. Adding an arbitrary firing threshold would be a separate model choice, not a deduction of the action potential's shape. More detailed models explicitly include ionic conductances. [S2]

Read [questions](questions.en.md) before [solutions](solutions.en.md). References: [S1–S3](../../sources/references.md). S3 is optional biological background, not the verification source for this derivation.
