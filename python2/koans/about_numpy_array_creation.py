#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import numpy as np
from itertools import product

class AboutNumpyArrayCreation(Koan):
    def test_create_empty(self):
        ar = np.array([])
        self.assertEqual((0,), ar.shape)
        
    def test_create_from_lists(self):
        # the simplest array construction takes a list of values
        ar = np.array([1,2,3])
        self.assertEqual((3,), ar.shape)
        # nested lists create multi-dimensional arrays
        ar = np.array([[1,2,3], [4,5]])
        self.assertEqual((2,), ar.shape)
        ar = np.array([[1,2,3], [4,5,6]])
        self.assertEqual((2,3), ar.shape)
        ar = np.array([[1,2], [4,5], [6,7]])
        self.assertEqual((3,2), ar.shape)

    def test_create_special(self):
        # create from defined 'patterns' with dynamic shape
        ar = np.ones((2,2))
        self.assertEqual((2,2), ar.shape)
        self.assertEqual(1, ar[0,0])
        self.assertEqual(1, ar[1,1])
        ar = np.zeros((3,3,3))
        self.assertEqual((3,3,3), ar.shape)
        self.assertEqual(0, ar[2,2,2])
        # numpy array-range works like builtin range
        ar = np.arange(3)
        self.assertArrayEqual(np.array([0, 1, 2]), ar)
        ar = np.identity(2)
        self.assertArrayEqual(np.array([[1,0], [0,1]]), ar)

    def test_create_with_cast(self):
        ar1 = np.array([1,2],dtype=float)
        ar2 = np.array([1,2],dtype=int)
        ar3 = np.array([1,2],dtype=complex)
        self.assertEqual(1.0, ar1[0])
        self.assertEqual(1, ar2[0])
        self.assertEqual((1+0j), ar3[0])
        self.assertEqual(True, ar1[0] == ar2[0])
