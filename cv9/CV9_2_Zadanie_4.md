## Zadanie 4 (5b)

V tomto zadaní budete pracovať s nástrojom MetaboAnalyst a datasetom: **NMR spectral bins**
    
`Binned 1H NMR spectra of 50 urine samples using 0.04 ppm constant width (Psihogios NG, et al.) Group 1- control; group 2 - severe kidney disease.`
    
Tento dataset je dostupný v sekcii 'Try our test data' v nástroji pre Jednofaktorovú štatistickú analýzu. 

Dataset pochádza z NMR-metabolomickej štúdie: Hodnotenie závažnosti tubulointersticiálnych lézií u pacientov s glomerulonefritídou. Začiatok tubulointersticiálnych lézií je charakterizovaný zníženým vylučovaním citrátu, hipurátu, glycínu a kreatinínu, zatiaľ čo po ďalšom zhoršení nasleduje glykozúria, selektívna aminoacidúria, úplné vyčerpanie citrátu a hipurátu a postupné zvyšovanie vylučovania laktátu, acetátu a trimetylamín-N-oxidu. Metabonomická analýza moču založená na NMR by mohla prispieť k včasnému hodnoteniu závažnosti poškodenia obličiek a prípadne k monitorovaniu ich funkcie. [1]


Načítajte množinu údajov v nástroji MetaboAnalyst. Pri filtrovaní údajov (Data filter) môžete použiť predvolené nastavenia.

### Úloha 1 (1b)

Normalizujte distribúciu datasetu (pre premenné aj vzorku).
(Vyberte akúkoľvek kombináciu operácií, ktorá je podľa Vás najlepšia).

**Ktoré operácie ste pri normalizácii použili?**
Sample normalization: Normalization by median
Data Transformation:  Square root transformation (square root of data values)
Data Scaling:         Auto scaling	(mean-centered and divided by the standard deviation of each variable)
### Úloha 2 (4b)

Použite ľubovoľné štatistické metódy na analýzu datasetu (napr. t-test, correlations, PCA, PLS-DA, Dendrogram, Heatmap, K-means, RandomForest, ..) 

**Uveďte aspoň 4 skutočnosti (z 4 rôznych metód), ktoré ste zistili analýzou datasetu:**

(Napr. Pri použití pearsonovho korelačného koeficientu je najvyššia pozitívna korelácia medzi premennými x a y, a koeficient korelácie je 0.992.)
1: PCA
   -pomocou PCA analýzy som vytvorila 2D Scores Plot pre prvú a druhú hlavnú komponentu (PC1 a PC2), spolu vysvetľujú takmer 40 % variability dát 
   -graf ukazuje jasné oddelenie kontrolnej skupiny od pacientov pozdĺž osi PC1 (24,9 %)
   -štatistická významnosť tohto rozdelenia bola potvrdená testom PERMANOVA s p-hodnotou 0,001
   -z grafu je vidieť, že skupina pacientov vykazuje oveľa vyššiu mieru variability než kontrolná skupina
2: Heatmap
   -top 5 premenných potvrdilo rozdelenie skupín 
   -u chorých pacientov je viditeľný výrazný pokles (modrá farba) pri  Bin.0.94, Bin.0.82 a Bin.8.74
   -Bin.2.54 a Bin.2.70 naopak potvrdzujú zvýšenie 
   -tieto trendy z nich robia kľúčové biomarkery pre identifikáciu ochorenia
3: Random Forest
   -Random Forest vykazuje presnosť s chybovosťou 0,06
   -kontrolnú skupinu klasifikoval bez chyby
   -u pacientov došlo k chybe pri 3 vzorkách
   -analýza odľahlých hodnôt odhalila, že vzorka P113 je najvýraznejším outlineom
4: Correlations
   -odhalili sme klastre pozitívne korelovaných premenných označených tmavočervenou, čo naznačuje, že skupiny pochádzajú z rovnakých biochemických dráh
   -niektoré biny vykazujú koreláciu blížiacu sa k hodnote 1.0
   -modré oblasti naznačujú negatívnu koreláciu, teda že nárast jednej látky je spojený s poklesom inej

Vygenerujte report z vykonanej analýzy a celý výsledný zip file odovzdajte ako prílohu k riešeniu zadania.

----

#### Referencie

[1] Psihogios, N. G., Kalaitzidis, R. G., Dimou, S., Seferiadis, K. I., Siamopoulos, K. C., & Bairaktari, E. T. (2007). Evaluation of tubulointerstitial lesions’ severity in patients with glomerulonephritides: an NMR-based metabonomic study. Journal of Proteome Research, 6(9), 3760–3770. https://doi.org/10.1021/PR070172W
