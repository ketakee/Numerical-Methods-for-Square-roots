#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  newton_raphson.py
#  
#  Copyright 2016 Ketakee Nimavat <Ketakee Nimavat@KETAKEE>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

#Function f
import math 
def f(x):
	return x**3 - 3*x*x + 7*x -8
	
#function f'

def diff(x,h):
    return ((f(x+h)-f(x-h))/(2*h))
  
def newton_raphson(a,c):
	c+=1
	if c<20:
		d=a- (f(a)/diff(a,0.05))
		d=round(d,5)
		print(c)
		print("a",round(a,5))
		print("f(a)",round(f(a),5))
		print("f'a",round(diff(a,0.05),5))
		print("d",round(d,5))
		print("F(d)", round(f(d),5))
		print()
		newton_raphson(round(d,5),round(c,5))

newton_raphson(1,0)

