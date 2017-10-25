#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Reg_falsi.py
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
import math
def f(x):
	return x**3 + x -1

def reg_falsi(a,b,c):
	c+=1
	print()
	print("test case c",c)
	print("a ",a)
	print("b ",b)
	print("f(a)",round(f(a),5),"fb",round(f(b),5))
	if c<20:
		if f(a)*f(b)<0:
			d=round((a*f(b) - b*f(a))/(f(b)-f(a)),5)
			print("d ", round(d,5))
			print('f(d)',round(f(d),5))
			if f(a)*f(d)>0:
				a=d;
			else:
				b=d
		return reg_falsi(a,b,c)
		
reg_falsi(0,1,0)
