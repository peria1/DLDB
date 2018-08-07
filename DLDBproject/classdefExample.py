r# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 12:40:37 2018

@author: Bill
"""

class Rectangle:
   def __init__(self, length, breadth, unit_cost=0):
       self.length = length
       self.breadth = breadth
       self.unit_cost = unit_cost
   
   def get_perimeter(self):
       return 2 * (self.length + self.breadth)
   
   def get_area(self):
       return self.length * self.breadth
   
   def calculate_cost(self):
       area = self.get_area()
       return area * self.cost
# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
#r = Rectangle(160, 120, 2000)
#print("Area of Rectangle: %s cm^2" % (r.get_area()))
#print("Cost of rectangular field: Rs. %s ", %(r.calculate_cost()))