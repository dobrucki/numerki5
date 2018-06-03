import matplotlib.pyplot as plt
# Stablicowane miejsca zerowe wielomianów wraz z wagami Laguerre'a
zeroes = [[0.585786437627, 3.414213562373], [0.415774556783, 2.294280360279, 6.289945082937],[0.322547689619, 1.745761101158, 4.536620296921, 9.395070912301],[0.263560319718, 1.413403059107, 3.596425771041, 7.085810005859, 12.640800844276]]
weights = [[0.853553390593, 0.146446609407], [0.711093009929, 0.278517733569, 0.0103892565016], [0.603154104342, 0.357418692438, 0.0388879085150, 0.000539294705561],[0.521755610583, 0.398666811083, 0.0759424496817 , 0.00361175867992, 0.0000233699723858]]

def horner(args, x):
    if args:
        res = 0
        for arg in args:
            res *= x
            res += arg
        return res
    return None

def gauss(nodes, f, stopien):
	wynik = 0
	i = 0
	while i < nodes:
		wynik += weights[nodes-2][i] * f(zeroes[nodes-2][i]) * lagPolynomial(stopien, zeroes[nodes-2][i])
		i += 1
	return wynik

def rysuj(a, b, step, f, wspolczynnikiWielomianuApr):
    tabX1 = []
    tabY1 = []
    tabY2 = []
    i = 0
    tmp = a
    while tmp <= b:
        tabX1.append(tmp)
        tabY1.append(f(tmp))
        wynik = 0
        for a in range(len(wspolczynnikiWielomianuApr)):
            wynik += wspolczynnikiWielomianuApr[a] * lagPolynomial(a, tmp)
        tabY2.append(wynik)
        tmp += step
        i += 1
    plt.plot(tabX1, tabY1, 'r-', label="f. aproksymowana")
    plt.plot(tabX1, tabY2, 'b-', label="f. aproksymująca")
    plt.legend()
    plt.show()

def lagPolynomial(stopien, x):
    L = []
    L.append(1)
    L.append(1-x)
    if stopien==0:
        return L[0]
    elif stopien==1:
        return L[1]
    else:
        i = 2
        while i <= stopien:
            k = i - 1
            wynik = 0
            wynik = (2*k+1-x) * L[k] - k*L[k-1]
            wynik /= k+1
            L.append(wynik)
            i += 1
        return wynik

def wspolczynniki(stopienWielomianuApr, wezlyGauss, f):
    wspolczynnikiWielomianuApr = []
    for a in range(stopienWielomianuApr + 2):
        wspolczynnikiWielomianuApr.append(gauss(wezlyGauss, f, a))
    return wspolczynnikiWielomianuApr
