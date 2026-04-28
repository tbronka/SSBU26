## Zadanie 3 (5b)

V tomto zadaní budete pracovať s nástrojom FamLinkX a datasetom **dna_screening_zadanie** dostupným v priečinku `inputs`. 

Dataset obsahuje údaje matky, dcéry a dvoch strýkov, ktorí sú bratmi muža, u ktorého predpokladáme, že je otcom dcéry. Je potrebné potvrdiť alebo vyvrátiť či bol muž otcom dievčaťa. Pomocou nástroja FamLinkX zostavte hypotézy s rodokmeňom členov, vykonajte analýzu, určte výsledné pravdepodobnosti hypotéz a uveďte výsledné rozhodnutie na potvrdenie/zamietnutie otcovstva.

<img src="data/family_tree.png" width="100%"/>

### Úloha 1 (1b)

**Formulujte hypotézy pre riešenie úlohy:**

H0 - muž je otcom dcéry a muži S1 a S2 sú strýkovia dieťaťa
HA - muž nie je otcom dcéry bez príbuzenského vzťahu s mužmi S1 a S2

### Úloha 2 (4b)

  Vykonajte analýzu pomocou nástroja FamLinkX. Ako referenčnú databázu použite Českú alebo Nemeckú databázu. Ako prílohu zadania odovzdajte vygenerovaný report z analýzy (Case report vo formáte .rtf). 

- referenčná databáza: česká

**Uveďte LR a pravdepodobnosť (W) pre jednotlivé hypotézy a Váš záver analýzy:**

W(H0) = 0,108657 / (0,108657 + 1) = 0,09800777

W(HA) = 1 - 0,09800777 = 0,90199223

**Hypotéza HA je výrazne pravdepodobnejšia (W(HA) 90,2% a LR 0,1087).
Otcovstvo nie je možné potvrdiť, ani vyvrátiť, no výsledky naznačujú, že otec nie je biologickým otcom dieťaťa.**