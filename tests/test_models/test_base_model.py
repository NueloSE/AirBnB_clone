#!/usr/bin/python3
"""
This module is for implementation of test cases
"""
import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
	"""
	Unit tests for the BaseModel class
	"""
	
	def test_init(self):
		"""
		Test that the __init__ method sets the id, create_at, and update_at attributes
		"""
		bm = BaseModel()
		self.assertIsInstance(bm.id, str)
		self.assertIsInstance(bm.created_at, datetime.datetime)
		self.assertIsInstance(bm.updated_at, datetime.datetime)

	def test_str(self):
		"""
		Test that the __str__ method returns a string representation of the object
		"""
		bm = BaseModel()
		str_repr = str(bm)
		self.assertIsInstance(str_repr, str)
		self.assertIn(bm.id, str_repr)
		self.assertIn(bm.__class__.__name__, str_repr)

	def test_save(self):
		"""
		Test that the save method updates the updated_at attribute
		"""
		bm = BaseModel()
		first_update = bm.updated_at
		bm.save()
		self.assertNotEqual(first_update, bm.updated_at)

	def test_to_dict(self):
		"""
		Test that the to_dict method returns a dictionary representation of the object
		"""
		bm = BaseModel()
		dict_repr = bm.to_dict()
		self.assertIsInstance(dict_repr, dict)
		self.assertIn('__class__', dict_repr)
		self.assertIn("id", dict_repr)
		self.assertIn('created_at', dict_repr)
		self.assertIn('updated_at', dict_repr)
		self.assertEqual(dict_repr['__class__'], bm.__class__.__name__)

if __name__ == "__main__":
	unittest.main()
