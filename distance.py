#!/usr/bin/env python3
#*-*coding: utf-8 *-*
#Autor: EdwardRamos
#Date: 10/21/2016 U.S.A


import math
x1 = int(input('Insert value x1: '))
y1 = int(input('Insert value y1: '))
x2 = int(input('Insert value x2: '))
y2 = int(input('Insert value y2: '))
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx ** 2 + dy ** 2
    print('dsquared is:', dsquared)
    result = int(math.sqrt(dsquared))    
    return result
print(distance(x1, y1, x2, y2))

