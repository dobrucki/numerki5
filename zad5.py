#!/usr/bin/python

import os
import math
import sys

#f_x = "math.sqrt(x)"
f_x = "{x}**3 + 3*{x}**2 + 6*{x} + 6"
#f_x = sys.stdin.readline().replace('\n','')
a = 1
#a = int( sys.stdin.readline().replace('\n','') )
maxL = 2

gnuplot_b = 20
f_x2 = f_x.replace('{x}','(x-(' + str(a) + '))' )
f_x = f_x.replace('{x}','x')


eps = 0.001

MIN_INF = 1000
SIMPSON_PODZIALY = 1000

def doPlot( f_x, wyn, a, b ):
	f = open( "plot.template" )
	plot_file = f.read()
	f.close()
	f = open ("plot", "w" )
	f.write( plot_file.replace('{F_X}', f_x ).replace('{WYN}', wyn ).replace('{A}', str(a) ).replace('{B}', str(b) ).replace('math.','') )
	f.close()
	os.system('gnuplot < ./plot 2>/dev/null')

def Simpson(func, a, b, n=1000):
	if n%2 == 0:
		n = n+1
	h = 1. * (b-a)/n
	C = 0
	x = a
	for i in range( n/2 + 1 ):
		y0 = eval( func )
		x = x + h
		y1 = eval( func )
		x = x + h
		y2 = eval( func )
		C = C + 1. * h/3 * ( y0 + 4*y1 + y2 )
	return C

def Simpson0Inf( func, eps ):
	a = 0
	e = 1
	D = eps
	C = 0
	while D >= eps or e < MIN_INF:
		D = Simpson( func, a, e, SIMPSON_PODZIALY )
		C =	C + D
		a = e
		e = e*10
	return C

def Netw(n,k):
	sum = 1
	for i in range( 1, k+1 ):
		sum = sum*(n-i+1)
		sum = sum/i
	return sum

def Silnia( n ):
	if n < 2:
		return 1
	return n*Silnia(n-1)

def add( a, b, ka=1, kb=1 ):
	la = len( a )
	lb = len( b )
	lmin = min( la, lb )
	T1 = [ ka*a[i]+kb*b[i] for i in range( lmin ) ]
	if la > lb:
		T2 = [ ka*a[i] for i in range( lmin, la ) ]
	else:
		T2 = [ kb*b[i] for i in range( lmin, lb ) ]
	return T1+T2


def L(n):
	return [ Netw( n, i ) * (-1)**i * 1. / Silnia( i ) for i in range( 0, n+1 ) ]

def func( tab ):
	ret = ""
	for i in range( len( tab ) ):
		if tab[ i ] != 0:
			if len( ret ) > 0:
				ret = ret + " + "
			ret = ret + str( tab[ i ] )
			if i > 0:
				ret = ret + "*x"
			if i > 1:
				ret = ret + "**" + str( i )
	return ret

def myRound( Val, eps ):
	return eps * int( Val/eps + 0.5 )

Wa = []
for i in range( 0, maxL+1 ):
	C1 = Simpson0Inf( "math.exp(-x) * ( " + f_x2 + ") * (" + func( L(i) ) + " ) ", eps*eps )
	C2 = Simpson0Inf( "math.exp(-x) * (" + func( L(i) ) + " )**2", eps*eps )
	Wb = L(i)
	Wa = add( Wa, Wb, 1, C1/C2 )

for i in range( len( Wa ) ):
	Wa[i] = myRound( Wa[i], eps )

wyn = func( Wa )

print "Badana:         " + f_x
if a != 0:
	print "Badana(-a):     " + f_x2
	print "Znaleziona(-a): " + wyn
	wyn = wyn.replace( 'x', '( x + (' + str( a ) + ') )' )
	print "Znaleziona(?):  " + wyn
	for i in range( len( Wa ) ):
		for j in range( i ):
			Wa[j] = Wa[j] + Wa[i] * Netw( i, j ) * a ** ( i-j )
	wyn = func( Wa )
print "Znaleziona:     " + wyn

doPlot( f_x, wyn, a, gnuplot_b )
