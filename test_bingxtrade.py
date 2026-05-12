# test_bingxtrade.py
"""
Tests for BingXTrade module.
"""

import unittest
from bingxtrade import BingXTrade

class TestBingXTrade(unittest.TestCase):
    """Test cases for BingXTrade class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BingXTrade()
        self.assertIsInstance(instance, BingXTrade)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BingXTrade()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
