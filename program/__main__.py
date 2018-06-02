from functions import *
import matplotlib.pyplot as plt
from math import fabs, e

# Stablicowane miejsca zerowe wielomianów wraz z wagami Laguerre'a
zeroes = [[0.585786437627, 3.414213562373], [0.415774556783, 2.294280360279, 6.289945082937],[0.322547689619, 1.745761101158, 4.536620296921, 9.395070912301],[0.263560319718, 1.413403059107, 3.596425771041, 7.085810005859, 12.640800844276]]
weights = [[0.853553390593, 0.146446609407], [0.711093009929, 0.278517733569, 0.0103892565016], [0.603154104342, 0.357418692438, 0.0388879085150, 0.000539294705561],[0.521755610583, 0.398666811083, 0.0759424496817 , 0.00361175867992, 0.0000233699723858]]

def lagPoly(stopien, x):
    l0 = 1
    l1 = x - 1
    lk = l1
    lkm = l0
    tab = [l0, l1]
    i = 1
    while i < stopien:
        wynik = (x - 2 * i - 1) * lk - i*i*lkm
        tab.append(wynik)
        lkm = lk
        lk = wynik
        i += 1
    return tab

def gauss(nodes, args, lk):
	wynik = 0
	i = 0
	while i < nodes:
		wynik += weights[nodes-2][i] * horner(args, zeroes[nodes-2][i]) * lk
		i += 1
	return wynik

def aproksymacja(st, wielomian, x):
    tablica_L = lagPoly(st, x)
    tablica_A = []
    for l in tablica_L:
        tablica_A.append(gauss(st, wielomian, l))
    wynik = 0
    i = 0
    while i < len(tablica_L):
        wynik += tablica_L[i] * tablica_A[i]
        i += 1
    return wynik

def rysujWielomian(a, b, wielomian, st):
    tabX = []
    tabY = []
    tabYa = []
    step = fabs(b - a) / 20
    x = a
    for i in range(0, 20):
        tabX.append(x)
        tabY.append(horner(wielomian, x) * e**(-x))
        tabYa.append(aproksymacja(st, wielomian, x))
        x += step
    plt.plot(tabX, tabY, 'r-')
    plt.plot(tabX, tabYa, 'b-')
    plt.show()

# print("Podaj wpolczynniki: ")
# args = [float(x) for x in input().split()]
# while True:
#     x = float(input("Podaj x: "))
#     print("Wynik: ", horner(args, x))
#
# st = int(input("Podaj stopień wielomianu: ")) # stopien wielomianu aproksymujacego
# a = float(input("Podaj początek przedziału: "))
# b = float(input("Podaj koniec przedziału: "))
# nodes = int(input("Podaj liczbę węzłów (od 2 do 5): "))

st = int(input("Podaj stopien: "))
# print(lagPoly(st, 1))
wielomian = [5, -4, 1]
rysujWielomian(0, 1, wielomian, st)
