# Corrigé

*English version: [solutions.en.md](solutions.en.md).*

1. Au départ, $I_L=g_L(V-E_L)=0$. La pente initiale vaut donc $\dot V(0^+)=I_0/C_m$.
2. Poser $V_\infty=E_L+I_0R_m$. Alors $V(t)=V_\infty+(V_0-V_\infty)e^{-t/(R_mC_m)}$. Dériver pour vérifier l'équation, puis poser $t=0$ pour vérifier la condition initiale.
3. $10^6\,\Omega\times10^{-12}\,\mathrm F=10^{-6}\,\mathrm s$. Pour 100 MΩ et 100 pF, le coefficient vaut 10 000 : 10 000 µs = 10 ms. Ne pas oublier les coefficients numériques.
4. La capacité de 50 pF donne la pente initiale la plus forte. Les trois courbes tendent vers la même tension, car $I_0R_m$ est fixé.
5. La constante de temps $\tau_m$ et la variation finale de tension doublent toutes les deux ; la pente initiale est inchangée.
6. $R_m=\Delta V/I_0=(4\times10^{-3})/(40\times10^{-12})=100$ MΩ. $C_m=\tau_m/R_m=0{,}015/10^8=150$ pF. Ces estimations ne valent que dans les hypothèses du modèle passif.
7. Non. Le modèle ne contient ni dynamique de canaux actifs ni mécanisme de déclenchement. Une conclusion biologique exige des mesures supplémentaires et un modèle adapté.
8. $|Z|=R_m/\sqrt{1+(\omega\tau_m)^2}$, $\arg Z=-\arctan(\omega\tau_m)$, $f_c=1/(2\pi\tau_m)$. Pour 10 ms, $f_c\approx15{,}92$ Hz. C'est la fréquence de coupure du modèle passif, pas une limite universelle de la fréquence de décharge neuronale.
