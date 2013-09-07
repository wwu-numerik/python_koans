#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

import path_to_enlightenment
from sensei import Sensei
from writeln_decorator import WritelnDecorator

class Mountain:
    def __init__(self):
        self.stream = WritelnDecorator(sys.stdout)
        self.tests = path_to_enlightenment.koans()
        self.lesson = Sensei(self.stream)

    def walk_the_path(self, args=None):
        "Run the koans tests with a custom runner output."

        if args and len(args) >=2:
            args.pop(0)
            test_names = ["koans." + test_name for test_name in args]
            self.tests = unittest.TestLoader().loadTestsFromNames(test_names)
        self.tests(self.lesson)
        self.lesson.learn()
        return self.lesson
      
    def session(self, num):
      sessions = { 1: ['about_asserts', 'about_strings', 'about_none', 'about_lists', 'about_list_assignments', 
            'about_dictionaries', 'about_string_manipulation', 'about_tuples', 'about_methods'],
        2: ['about_control_statements', 'about_true_and_false', 'about_sets', 'about_triangle_project', 
            'about_exceptions', 'about_triangle_project2',],
        3: ['about_iteration', 'about_comprehension', 'about_generators', 'about_lambdas', 'about_scoring_project',],
        4: ['about_classes', 'about_new_style_classes', 'about_class_attributes', 'about_with_statements', 'about_dice_project',],
        5: ['about_inheritance', 'about_multiple_inheritance', 'about_scope', 'about_modules', 'about_packages',],
        6: ['numpy.about_array_creation', 'numpy.about_array_operations', 'numpy.about_array_views', 'numpy.about_equations', ], 
      }
      return self.walk_the_path(sessions[num])
            