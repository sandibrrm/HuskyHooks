# test_huskyhooks.py
"""
Tests for HuskyHooks module.
"""

import unittest
from huskyhooks import HuskyHooks

class TestHuskyHooks(unittest.TestCase):
    """Test cases for HuskyHooks class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HuskyHooks()
        self.assertIsInstance(instance, HuskyHooks)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HuskyHooks()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
