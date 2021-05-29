# import bibliotek
import json
import numpy as np


# definicja klasy graf
class Graf:
    krawedzie = []
    liczba_wierzcholkow = -1
    wierzcholek_startowy = -1


# funkcja odpowiedzialna za wyświetlenie wyników w konsoli
def pokaz_odleglosci(graf, dystans):
    szerokosc_naglowka = 56 + len(
        str(g.wierzcholek_startowy))  # 56 - liczba znaków "stałych", tj. poza długością liczby
    # będącej indeksem wierzchołka startowego
    print("–" * szerokosc_naglowka)
    print("| Wierzcholek | Odleglosc od wierzcholka poczatkowego", graf.wierzcholek_startowy, "|")
    print("=" * szerokosc_naglowka)
    # pętla odpowiedzialna za wyświetlanie w nowych wierszach odległości do kolejnych wierzchołków
    # w przypadku gdy wierzchołek jest nieosiągalny wyświetlana jest informacja "Nieosiagalny"
    for i in range(0, graf.liczba_wierzcholkow):
        print("| {:11s} | {:39s} |".format(str(i), str(dystans[i]) if dystans[i] != float(np.inf) else "Nieosiagalny"))
    print("–" * szerokosc_naglowka)


# algorytm Bellmana-Forda
def BellmanFord(graf):
    dystans = [float(np.inf)] * graf.liczba_wierzcholkow  # ustawiamy odleglość od kazdego wierzchołka na "inf"
    # algorytm daje możliwość znalezienia "poprzednika" danego wierzchołka na ścieżce od wierzchołka startowego
    # nie było to celem zadania, więc zostało zakomentowane
    # poprzednik = [None] * graf.liczba_wierzcholkow
    dystans[graf.wierzcholek_startowy] = 0

    for i in range(0, graf.liczba_wierzcholkow - 1):
        zmiana = False  # zmienna odpowiadająca za przechowywanie informacji czy w danym obiegu pętli nastąpiła jakaś aktualizacja dystansów
        for poczatek_krawedzi, koniec_krawedzi, waga_krawedzi in graf.krawedzie:
            if dystans[poczatek_krawedzi] + waga_krawedzi < dystans[koniec_krawedzi]:
                dystans[koniec_krawedzi] = dystans[poczatek_krawedzi] + waga_krawedzi
                zmiana = True
                # poprzednik[koniec_krawedzi] = poczatek_krawedzi
        if not zmiana:  # jeśli nie było zmian dystansu algorytm kończy pracę
            return pokaz_odleglosci(graf, dystans)

    # sprawdzenie czy występują cykle o ujemnej wadze
    for poczatek_krawedzi, koniec_krawedzi, waga_krawedzi in graf.krawedzie:
        if dystans[poczatek_krawedzi] + waga_krawedzi < dystans[koniec_krawedzi]:
            print("Wykryto cykl o ujemnej wadze")
            return

    return pokaz_odleglosci(graf, dystans)


with open("graf.json", "r") as file:  # otworzenie pliku "graf.json" z listą sąsiedztwa
    dane = json.load(file)
# tab = np.array(dane, dtype=object)

g = Graf()
g.liczba_wierzcholkow = len(dane) - 1
for i in range(0, g.liczba_wierzcholkow):
    for j in range(0, len(dane[i])):
        g.krawedzie.append([i, dane[i][j][0], dane[i][j][1]])

g.wierzcholek_startowy = dane[-1]  # wierzchołek startowy odczytany z pliku json

BellmanFord(g)