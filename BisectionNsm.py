#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  BisectionNsm.py
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
import math as m  
def f(x):
	return  x*x*x - 4*x-9


def bisection(a,b,c):
	print()
	print("test case c",c+1)
	print("a ",a)
	print("b ",b)
	print("c",round((a+b)/2,5))
	print("f(a+b)/2 ",round(f((a+b)/2),5))
	c+=1
	if c>=20:
		return a,b,a+b/2
	else:
		if f(a)>0 and f(b)<0:
			if f((a+b)/2)>0:
				a=round((a+b)/2,5)
			elif f((a+b)/2)<0:
				b=round((a+b)/2,5)
		else:
			if f((a+b)/2)<0:
				a=round((a+b)/2,5)
			elif f((a+b)/2)>0:
				b=round((a+b)/2,5)
		return bisection(a,b,c)
print(bisection(2,3,0))
