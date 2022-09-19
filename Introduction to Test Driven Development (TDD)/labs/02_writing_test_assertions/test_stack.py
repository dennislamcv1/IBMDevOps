from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Test cases for Stack"""

    def setUp(self):
        """Setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None

    def test_push(self):
        """Test pushing an item into the stack"""
        raise Exception("not implemented")

    def test_pop(self):
        """Test popping an item of off the stack"""
        raise Exception("not implemented")

    def test_peek(self):
        """Test peeking at the top the stack"""
        raise Exception("not implemented")

    def test_is_empty(self):
        """Test if the stack is empty"""
        raise Exception("not implemented")
