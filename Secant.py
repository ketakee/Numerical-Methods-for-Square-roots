#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  seacnt.py
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
	return m.cos(x) - x**0.5
	
def secant(a,b,i):
	if i<20:
		if f(b)!=f(a):
			c = b - (f(b)*(b-a))/(f(b)-f(a))
			print(c)
			i+=1
			return secant(b,c,i)
		else:
			return a,b
secant(2,3,0)
