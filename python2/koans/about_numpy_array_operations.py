#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import numpy as np

class AboutArrayOperations(Koan):
    
    def test_basic_math(self):
        ar = np.arange(3)
        ar *= 2
        self.assertArrayEqual(np.array([0, 2, 4]), ar)
        self.assertArrayEqual(np.array([0, 4, 16]), ar*ar)
        ar += 1
        self.assertArrayEqual(np.array([1, 3, 5]), ar)
        ones = np.ones(3)
        ar -= ones
        self.assertArrayEqual(np.array([0, 2, 4]), ar)
        ar -= [1,2,3]
        self.assertArrayEqual(np.array([-1,0,1]), ar)
        
    def test_vector_math(self):
        ar = np.array([1,2,3])
        scalar = ar.dot(ar)
        self.assertEqual(14, scalar)
        self.assertEqual(True, (scalar==np.inner(ar,ar)))
        A = np.array([[2,0], [0,-2]])
        x = np.array([-1,1])
        self.assertArrayEqual(np.array([-2, -2]), A.dot(x))
        a = np.array([1., 4., 0.]) 
        b = np.array([2., 2., 1.]) 
        self.assertArrayEqual(np.array([4., -1., -6.]), np.cross(a, b))
        self.assertArrayEqual(np.array([[ 2.,  2.,  1.], [ 8.,  8.,  4.],  [ 0.,  0.,  0.]]), np.outer(a, b))
            
    def test_comparison(self):
        ar = np.array([1,2,3])
        ko = np.array([1,2,3])
        self.assertEqual(True, np.array_equal(ar, ko))
        self.assertArrayEqual(np.array([True, True, True]), (ar == ko))
        self.assertEqual(True, (ar == ko).all())
        
    def test_norms(self):
        a = np.array([3,-4,5])
        norm = np.linalg.norm
        self.assertEqual(7.0710678118654755, norm(a))
        self.assertEqual(5, norm(a, np.inf))
        self.assertEqual(3, norm(a, -np.inf))