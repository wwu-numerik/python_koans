#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import numpy as np

class AboutArrayOperations(Koan):
    
    def test_basic_math(self):
        ar = np.arange(3)
        ar *= 2
        self.assertArrayEqual(__, ar)
        self.assertArrayEqual(__, ar*ar)
        ar += 1
        self.assertArrayEqual(__, ar)
        ones = np.ones(3)
        ar -= ones
        self.assertArrayEqual(__, ar)
        ar -= [1,2,3]
        self.assertArrayEqual(__, ar)
        
    def test_vector_math(self):
        ar = np.array([1,2,3])
        scalar = ar.dot(ar)
        self.assertEqual(__, scalar)
        self.assertEqual(__, (scalar==np.inner(ar,ar)))
        A = np.array([[2,0], [0,-2]])
        x = np.array([-1,1])
        self.assertArrayEqual(__, A.dot(x))
        a = np.array([1., 4., 0.]) 
        b = np.array([2., 2., 1.]) 
        self.assertArrayEqual(__, np.cross(a, b))
        self.assertArrayEqual(__, np.outer(a, b))
            
    def test_comparison(self):
        ar = np.array([1,2,3])
        ko = np.array([1,2,3])
        self.assertEqual(__, np.array_equal(ar, ko))
        self.assertArrayEqual(__, (ar == ko))
        self.assertEqual(__, (ar == ko).all())
        
    def test_norms(self):
        a = np.array([3,-4,5])
        norm = np.linalg.norm
        self.assertEqual(__, norm(a))
        self.assertEqual(__, norm(a, np.inf))
        self.assertEqual(__, norm(a, -np.inf))