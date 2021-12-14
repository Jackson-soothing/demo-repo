#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 18:01:03 2021

@author: soothing
"""

def Pascal_Triangle(N):
 
    for layer in range(1, N + 1):
        start = 1 
        for i in range(1, layer + 1):
      
            # The start value in a line is always 1
            print(start, end = " ")
            
            start = int(start * (layer - i) / i)
        
        # move next layer to new line
        print("")

#the 1st 4 layers
N = 4;
Pascal_Triangle(N)