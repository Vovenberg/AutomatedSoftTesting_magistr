# -*- coding: utf-8 -*-

import unittest
from pr2.app_calculate import Calculate

class TestCalculate(unittest.TestCase):
	def setUp(self):
		self.calc = Calculate()

	def test_add_universal_method_with_int_returns_correct_result(self):
		self.assertEqual(4, self.calc.add(2,2))
		self.assertEqual(5, self.calc.add(2,3))

	def test_add_universal_method_with_string_args_returns_correct_result(self):
		self.assertEqual("HelloWorld", self.calc.add("Hello","World"))

	def test_add_universal_method_with_array_args_returns_correct_result(self):
		self.assertEqual([1,3,4], self.calc.add([1,3], [4]))

	def test_add_method_returns_correct_result(self):
		self.assertEqual(4, self.calc.add_s(2,2))
		self.assertEqual(5, self.calc.add_s(2,3))

	def test_add_method_raises_typeerror_if_not_ints(self):
		self.assertRaises(TypeError, self.calc.add_s, "Hello","World")
		self.assertRaises(TypeError, self.calc.add_s, [1,3], [4])


if __name__ == '__main__':
	unittest.main()