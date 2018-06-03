from functions import *
from mathFunctions import *

wezlyGauss = 4
stopienWielomianuApr = 3
f = fun1
a = 1
b = 3
wspolczynnikiWielomianuApr = wspolczynniki(stopienWielomianuApr, wezlyGauss, f)
rysuj(a, b, 0.05, f, wspolczynnikiWielomianuApr)
