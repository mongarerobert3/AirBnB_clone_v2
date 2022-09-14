#!/usr/bin/python3
"""Unittest User"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test class for User"""

    def __init__(self, *args, **kwargs):
        """Test allows us to access methods of the base class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test if first name is string"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test if last name is string"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Teste if email is string"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Test if password is string"""
        new = self.value()
        self.assertEqual(type(new.password), str)
