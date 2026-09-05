# R65 — Décision de passage vers R66

~~~text
R65_PIPELINE = GO
R66 = AUTHORIZED_WITH_PLATFORM_LOCK
ARTICLE_1_SUBMISSION_STATUS = UNCHANGED_HOLD
MICROMETRIC_CLAIM = FORBIDDEN
~~~

R65 valide l'outil, pas DDF. La prochaine ronde peut donc tester une vraie
approximation métrique, mais elle doit choisir **une seule** plateforme avant
le calcul.

Deux routes restent possibles :

| Route | Avantage | Coût/risque |
|---|---|---|
| géométrie résolue R63/POLY944 | continuité directe avec le noyau DDF-G validé | périodes, fond D7/O7, warping et stabilisation à reconstruire pour cette géométrie |
| plateforme POLY925 publiée | données physiques antérieures plus proches d'un fond D7/O7 | ne démontre rien sur la géométrie R63 ; identité de fond et lissage à certifier séparément |

R66 ne doit pas combiner la famille de lissage de la première route avec les
flux, périodes ou tadpoles de la seconde. Le premier livrable R66 sera donc
un manifeste d'identité de plateforme ; l'approximation métrique et le
spectre ne commenceront qu'après ce verrou.


