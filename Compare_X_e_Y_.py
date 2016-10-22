#!/usr/bin/env python3
#Autor: Edward Ramos
#Date: 10/21/2016


#Funcao compare 
#1 se x > y
#0 se x == y
#-1 se x < y

x = int(input('Insert valor de X: '))
y = int(input('Insert valor de Y: '))

def compare(x, y):
    if x > y:
        print (1)
    if x == y:
        print (0)
    if x < y:
        print (-1)
compare(x, y)
