## Zadanie 2 (5b)

V tomto zadaní budete pracovať s aplikáciou v adresári `machine_learning` a datasetom: **Breast Cancer Wisconsin (Diagnostic)**

Dataset je dostupný aj online samostatne, alebo v knižnici scikit-learn: 
https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html

Dataset Breast Cancer Wisconsin (Diagnostic) obsahuje údaje získané z digitalizovaných obrazov tenkých ihlových aspirátov (FNA) hmoty prsníka, ktoré opisujú charakteristiky jadier buniek v nich. Zahŕňa 569 prípadov s 30 vlastnosťami, s cieľom na klasifikáciu benigných alebo maligných prípadov rakoviny prsníka na základe rôznych vlastností jadier buniek. Viac informácií nájdete na UCI Machine Learning Repository. [1]

### Úloha 1 (1b)

Pridajte do kódu ďalší model strojového učenia (ľubovoľný), a taktiež definujte parametre a ich hodnoty pre Grid Search.

**Uveďte aký ML model a hodnoty jeho parametrov ste použili:**

# SVC = SUpport Vector Classifier s polynomiálnym jadrom
- volím model SVC, nakoľko mojou prvou myšlienkou bolo použitie nejakého typu regresie (poisson/gama), no po debate s AI som usúdila, že tento typ nie je na daný dataset vhodný a preto volím SVC 
Hodnoty parametrov:
    - C -> 0.6
    - kernel -> 'linear' (najskôr som chcela zvoliť 'poly', no pre čas som to upravila na linear)
    - gamma -> ['scale', 0.01, 0.1] => nižšie aby som predišla overfitting-u

### Úloha 2 (2b)

Implementujte ďalšiu (ľubovoľnú) metriku pre evaluáciu modelov. Nezabudnite na to, aby sa implementovaná metrika ukladala do logov v súbore `model_accuracies.csv` a tiež ju pridajte do grafov (do grafov pre funkciu hustoty rozdelenia a tiež pre ňu vytvorte nový graf ktorý bude zobrazovať jej priebeh počas replikácií - tak ako pre presnosť (accuracy)).  

**Uveďte akú metriku ste doplnili:**

Recall - správna identifikácia TP / (TP + FN) (skutočne pozitívnych)

### Úloha 3 (1b)

Do implementácie pridajte ukladanie všetkých grafov, ktoré sa vytvárajú pri behu skriptu `main.py`` v adresári `machine_learning`.

### Úloha 4 (1b)

**V skripte `main.py`** nastavte počet replikácií na vyššie číslo (rozumne, podľa vlastného uváženia). Vykonajte beh aplikácie s Vašou implementáciou. Po skončení behu zanalyzujte vygenerované grafy a pár vetami popíšte ich interpretáciu. (Napr. v čom je ktorý ML model lepší, a pod.)

- model som skúšala spustiť na 50 replikácií, no v noci mi bohužiaľ spadol, tak som pristúpila k 20

### Interpretácia
- oba modely sú spoľahlivé nad 0.95, no model SVC je presnejší, nakoľko jeho vrchol je užší a teda stabilnejší
- priemerná presnosť oboch modelov je vysoká => dokonca logistická regresia vyšla lepšie
- priemerná chyba false negatives je pre SVC nižšia o 0.2 a teda SVC prehliadne menej chorých ako logistická regresia

### Najlepšie zvolené parametre pre SVC:
- coef0 = 0
- degree = 3
- gamma = scale
----

#### Referencie

[1] Street, W. N., Wolberg, W. H., & Mangasarian, O. L. (1993). Nuclear feature extraction for breast tumor diagnosis. Electronic Imaging, 1905, 861–870. https://doi.org/10.1117/12.148698
