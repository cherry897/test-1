# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 14:28:20 2023

@author: Student
"""

class cal:
    def __init__(self,a,b):
        self.v=a
        self.g=b
        print("this init got executed.")
    def add1(self):
        print(self.v+self.g)
    def sub1(self):
        print(self.v-self.g)
    def mul(self):
        print(self.v*self.g)