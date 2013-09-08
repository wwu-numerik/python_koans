#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import numpy as np

class AboutArrayViews(Koan):
    
    def test_slicing(self):
        ar = np.arange(9)
        self.assertArrayEqual(__, ar[1:3])
        self.assertArrayEqual(__, ar[1:7:2])
        ar = np.array([[1, 2], [3, 4], [5, 6]])
        self.assertArrayEqual(__, ar[1:3])

    def test_iteration(self):
        ar = np.ones((5,))
        for x in ar:
            self.assertArrayEqual(__, x)
        ar = np.ones((5,5))
        for x in ar:
            self.assertArrayEqual(__, x)
            
    def test_views_allow_edits(self):
        ar = np.array([[1, 2], [3, 4], [5, 6]])
        view = ar[2]
        view[0] += 2
        view[1] = -42
        self.assertArrayEqual(__, ar)
        self.assertEqual(__, type(view))