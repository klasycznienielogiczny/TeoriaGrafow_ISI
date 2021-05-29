# Teoria Grafów ISI 2020/2021
 Repozytorium zawierające pliki wykonanego projektu z teorii grafów

Część analityczna znajduje się w całości w pliku _Paluch_projekt_TG_cz_analityczna.pdf_
Część programistyczna znajduje się w dwóch plikach:
* plik _BellmanFord.py_ zawiera implementację algorytmu Bellmana-Forda w języku Python
* plik _Paluch_projekt_TG_cz_projektowa.pdf_ zawiera analizę algorytmu

## Program wymaga grafu w postaci listy sąsiedztwa!

## Instrukcja uruchomienia projektu

Aby uruchomić projekt wystarczy sklonować repozytorium lub skopiować zawartość pliku
_BellmanFord.py_ do środowiska programistycznego Python (polecane PyCharm, Google Colab,
Mu, itp.). Należy upewnić się, że zainstalowana jest biblioteka NumPy oraz json. Należy
wskazać nazwę pliku (w przypadku gdy znajduje się w tym samym folderze) lub ścieżkę do 
pliku json zawierającego graf w postaci listy sąsiedztwa (opis w następnym punkcie). 
Domyślna nazwa _graf.json_. Istnieje możliwość podania grafu z pliku pod inną nazwą, 
w tym celu należy w linii 55 zamiast _"graf.json"_ wpisać właściwą nazwę pliku wraz z 
rozszerzeniem.

## Wytyczne do pliku zawierajacego graf w postaci listy sąsiedztwa

Przykładowa zawartość pliku _graf.json_:

```json
[[[2,1], [1, 2], [4, 8], [10, 5], [3, 7], [9, 7], [6, 8]], 
[[6, 1], [3, 0], [0, 8], [2, 8], [8, 3], [4,12]], 
[[0, 1], [5, 8], [11, 7], [8, 7], [4, 5], [1, 8], [6,1]], 
[[7, 3], [10, 8], [1, 4], [9, 7], [5, 1], [11, 7], [8, 3], [0, 5]], 
[[6, 7], [8, 5], [2, 4], [0, 4], [1, 6]], 
[[7, 5], [2, 8], [3,8]], 
[[4, 2], [1, 7], [8, 2], [0, 7], [2, 2]], 
[[3, 7], [5, 5], [10, 8], [8, 7]], 
[[9, 0], [2, 7], [6, 6], [4, 4], [11,11], [1, 10], [3, 5], [10, 10], [7, 7]], 
[[8, 1], [11, 4], [3, 2], [10, 3], [0, 1]], 
[[3, 3], [7, 2], [9, 0], [0, 4], [8, 2]], 
[[9, 7], [2, 8], [8, 1], [3, 9]],
[[9,8]],
0
]
```

Graf podawany jest w postaci "listy list".

Numer wiersza odpowiada numerowi wierzchołka (numer wierzchołka nie jest podawany jawnie),
nowy wiersz to nowy wierzchołek grafu i nowy element listy, oddzielony przecinkiem od poprzedniego.
W każdym wierszu podawana jest lista sąsiedztwa w postaci (dwuelementowych) tablic z 
informacją o numerze wierzchołka końcowego krawędzi (pierwsza liczba) i wadze danej krawędzi 
(druga liczba), wierzchołkiem początkowym krawędzi jest wierzchołek mający numer aktualnie 
rozpatrywanego wiersza (elementu listy).
Na ostatniej pozycji (ostatni wiersz przed nawiasem zamykajacym) podany jest numer wierzchołka
startowego.

Ogólny schemat:
[ [ [wierzchołek końcowy krawędzi, waga krawędzi], kolejne krawędzie od tego samego wierzchołka początkowego],
kolejne wierzchołki początkowe, numer wierzchołka startowego]

## Rezulat wykonania programu dla powyższego grafu
```angular2html
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––
| Wierzcholek | Odleglosc od wierzcholka poczatkowego 0 |
=========================================================
| 0           | 0                                       |
| 1           | 2                                       |
| 2           | 1                                       |
| 3           | 2                                       |
| 4           | 4                                       |
| 5           | 3                                       |
| 6           | 2                                       |
| 7           | 5                                       |
| 8           | 4                                       |
| 9           | 4                                       |
| 10          | 5                                       |
| 11          | 8                                       |
| 12          | Nieosiagalny                            |
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––
```

### Rezoulat wykonania programu dla grafu z cyklem o ujemnej wadze
**Przykładowy graf**
```json
[[[2,1], [1, 2], [4, 8], [10, 5], [3, 7], [9, 7], [6, 8]], 
[[6, 1], [3, 0], [0, 8], [2, 8], [8, 3], [4,12]], 
[[0, -1], [5, 8], [11, -7], [8, 7], [4, 5], [1, 8], [6,1]],
[[7, 3], [10, 8], [1, 4], [9, 7], [5, 1], [11, 7], [8, -3], [0, -5]],
[[6, -7], [8, 5], [2, 4], [0, -4], [1, 6]],
[[7, 5], [2, 8], [3,8]], 
[[4, 2], [1, 7], [8, 2], [0, 7], [2, 2]], 
[[3, 7], [5, 5], [10, 8], [8, 7]], 
[[9, 0], [2, 7], [6, 6], [4, 4], [11,-11], [1, 10], [3, 5], [10, -10], [7, 7]],
[[8, 1], [11, 4], [3, 2], [10, 3], [0, 1]], 
[[3, -3], [7, -2], [9, 0], [0, 4], [8, 2]],
[[9, 7], [2, 8], [8, 1], [3, 9]],
[[9,8]],
0
]
```


**Rezultat**
```angular2html
Wykryto cykl o ujemnej wadze
```
