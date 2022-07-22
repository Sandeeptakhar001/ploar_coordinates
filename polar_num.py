# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:59:31 2022

@author: EVOL
"""
import cmath
import math


command  = complex(input())
r = math.sqrt(abs(command.real**2) + abs(command.imag**2))
phase = cmath.phase(command)
print(r)
print(phase)
