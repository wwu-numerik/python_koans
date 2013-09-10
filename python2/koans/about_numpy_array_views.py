#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import numpy as np

class AboutArrayViews(Koan):
    
    def test_slicing(self):
        ar = np.arange(9)
        # slice one dimensional arrays just like python lists
        self.assertArrayEqual(__, ar[1:3])
        # or with an non-default increment
        self.assertArrayEqual(__, ar[1:7:2])
        ar = np.array([[1, 2], [3, 4], [5, 6]])
        # with 2-dim arrays we can slice in each dim
        self.assertArrayEqual(__, ar[1,:])
        self.assertArrayEqual(__, ar[:,1])
        self.assertArrayEqual(__, ar[1:3,0])
        
    def test_iteration(self):
        ar = np.ones((5,))
        for x in ar:
            self.assertEqual(__, x)
        ar = np.ones((5,5))
        for x in ar:
            self.assertArrayEqual(__, x)
            
    def test_views_allow_edits(self):
        ar = np.array([[1, 2], [3, 4], [5, 6]])
        # a view references underlying memory
        view = ar[2]
        view[0] += 2
        view[1] = -42
        self.assertArrayEqual(__, ar)
        self.assertEqual(__, type(view))