#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
import numpy as np

class AboutArrayCreation(Koan):
  
  def test_create_empty(self):
    ar = np.array()
    self.assertEqual(__, len(ar))