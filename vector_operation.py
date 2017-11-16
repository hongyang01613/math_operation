# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:23:09 2017

@author: admin
"""
import math
from decimal import Decimal, getcontext

class Vector():
  
  CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
  
  def __init__(self,coordinates):
    try:
      if not coordinates:
        raise ValueError
      self.coordinates = tuple([Decimal(x) for x in coordinates])
      self.dimension = len(self.coordinates)
      
    except ValueError:
      raise ValueError('The coordinates must be nonempty')
      
    except TypeError:
      raise TypeError('The TypeError')
  
  def plus(self,v):
    new_coordinates = [x + y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)
  
  def minus(self,v):
    new_coordinates = [x - y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)
  
  def times_scalar(self, c):
    new_coordinates = [c * x for x in self.coordinates]
    return Vector(new_coordinates)
  
  def magnitude(self):
    coordinates_squared = [x ** 2 for x in self.coordinates]
    return math.sqrt(sum(coordinates_squared))
  
  def normalized(self):
    try:
      magnitude = self.magnitude()
      return self.times_scalar(Decimal(1./magnitude))
    except ZeroDivisionError:
      raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
  
  def dot_product(self, v):
    return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
  
  def angle_with(self, v, in_degrees = False):
    try:
      u1 = self.normalized()
      u2 = v.normalized()
      angle_in_radians = math.acos(u1.dot_product(u2))
      
      if in_degrees:
        degrees_per_radian = 180./math.pi
        return angle_in_radians * degrees_per_radian
      else:
        return angle_in_radians
    except Exception as e:
      if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
        raise Exception('Cannot compute an angle with zero vector')
      else:
        raise e
        
  def is_orthogonal_to(self, v, tolerance = 1e-10):
    return abs(self.dot_product(v)) < tolerance
  
  def is_parallel_to(self, v):
    return (self.is_zero() or
            v.is_zero() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == math.pi )
  
  def is_zero(self, tolerance = 1e-10):
    return self.magnitude() < tolerance
  
  def projective_vector(self, v):
#    c = v.normalized()
#    b = self.dot_product(c)
    new_coordinates = [(self.dot_product(v.normalized)) * (v.normalized())]
    return Vector(new_coordinates)
  
  def __str__(self):
    return "Vector: {}".format(self.coordinates)
  
  def __eq__(self, v):
    return self.coordinates == v.coordinates
  
v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
print (v.is_parallel_to(w))  
print (v.is_orthogonal_to(w))

'''  
v = Vector([-0.221, 7.437])
print (v.dot_product())

p = Vector([5.581,-2.136])
print (p.normalized())
'''