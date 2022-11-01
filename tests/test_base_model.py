#!/usr/bin/python3
"""Testing the BaseModel class"""
from datetime import datetime
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    
    def setUp(self):
        """Instance of a BaseModel setup"""
        self.m1 = BaseModel()

    def tearDown(self):
        """Instance of a BaseModel tear down"""
        del self.m1

    def test_diff_id(self):
        """ tests to make sure both instances have different ids """
        m2 = BaseModel()
        self.assertNotEqual(self.m1.id, m2.id)

    def test_str(self):
        """ test to check the string representation """
        self.m1.name = "Nat"
        string = "[{}] ({}) {}".format(self.m1.__class__.__name__,
                                        self.m1.id,                                                                       self.m1.__dict__)
        self.assertEqual(str(self.m1), string)

    def test_format(self):
        """ test to check for time format """
        self.m1.save()
        m1_json = self.m1.to_dict()
        updated = self.m1.updated_at
        updated2 = datetime.strptime(m1_json["updated_at"],
                                    "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(updated, updated2)

    def test_attributes(self):
        """ tests attributes and save/update times """
        self.m1.name = "Nat"
        self.m1.my_number = 5

        self.assertTrue(self.m1.name, "Nat")
        self.assertTrue(self.m1.my_number, 5)

        created = self.m1.created_at
        updated = self.m1.updated_at
        self.m1.save()
        created2 = self.m1.created_at
        updated2 = self.m1.updated_at

        self.assertEqual(created, created2)
        self.assertNotEqual(updated, updated2)
