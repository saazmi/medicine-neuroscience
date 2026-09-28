# Solutions

*Version française (référence) : [solutions.md](solutions.md).*

1. $I_L=g_L(V-E_L)=0$ initially. Therefore $\dot V(0^+)=I_0/C_m$.
2. Let $V_\infty=E_L+I_0R_m$. Then $V(t)=V_\infty+(V_0-V_\infty)e^{-t/(R_mC_m)}$. Differentiate to check the ODE and set $t=0$ to check the initial condition.
3. $10^6\,\Omega\times10^{-12}\,\mathrm F=10^{-6}\,\mathrm s$. For 100 MΩ and 100 pF, the coefficient is 10,000: 10,000 µs = 10 ms. Do not forget the numerical coefficients.
4. $C_m=50$ pF has the steepest initial slope. All three approach the same voltage because $I_0R_m$ is fixed.
5. Both $\tau_m$ and the final voltage change double; the initial slope is unchanged.
6. $R_m=\Delta V/I_0=(4\times10^{-3})/(40\times10^{-12})=100$ MΩ. $C_m=\tau_m/R_m=0.015/10^8=150$ pF. These estimates are valid only under the passive-model assumptions.
7. No. The model contains no active channel dynamics or spike-generation mechanism. A biological inference requires additional measurements and an appropriate model.
8. $|Z|=R_m/\sqrt{1+(\omega\tau_m)^2}$, $\arg Z=-\arctan(\omega\tau_m)$, $f_c=1/(2\pi\tau_m)$. For 10 ms, $f_c\approx15.92$ Hz. This is the passive model's cutoff, not a universal upper limit on neuronal firing rates.
