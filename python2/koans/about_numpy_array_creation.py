#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import numpy as np
from itertools import product

class AboutNumpyArrayCreation(Koan):
    def test_create_empty(self):
        ar = np.array([])
        self.assertEqual(__, ar.shape)
        
    def test_create_from_lists(self):
        # the simplest array construction takes a list of values
        ar = np.array([1,2,3])
        self.assertEqual(__, ar.shape)
        # nested lists create multi-dimensional arrays
        ar = np.array([[1,2,3], [4,5]])
        self.assertEqual(__, ar.shape)
        ar = np.array([[1,2,3], [4,5,6]])
        self.assertEqual(__, ar.shape)
        ar = np.array([[1,2], [4,5], [6,7]])
        self.assertEqual(__, ar.shape)

    def test_create_special(self):
        # create from defined 'patterns' with dynamic shape
        ar = np.ones((2,2))
        self.assertEqual(__, ar.shape)
        self.assertEqual(__, ar[0,0])
        self.assertEqual(__, ar[1,1])
        ar = np.zeros((3,3,3))
        self.assertEqual(__, ar.shape)
        self.assertEqual(__, ar[2,2,2])
        # numpy array-range works like builtin range
        ar = np.arange(3)
        self.assertArrayEqual(__, ar)
        ar = np.identity(4,14,3)
        self.assertArrayEqual(__, ar)

    def test_create_with_cast(self):
        ar1 = np.array([1,2],dtype=float)
        ar2 = np.array([1,2],dtype=int)
        ar3 = np.array([1,2],dtype=complex)
        self.assertEqual(__, ar1[0])
        self.assertEqual(__, ar2[0])
        self.assertEqual(__, ar3[0])
        self.assertEqual(__, ar1[0] == ar2[0])
