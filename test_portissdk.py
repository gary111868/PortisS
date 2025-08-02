# test_portissdk.py
"""
Tests for PortisSDK module.
"""

import unittest
from portissdk import PortisSDK

class TestPortisSDK(unittest.TestCase):
    """Test cases for PortisSDK class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortisSDK()
        self.assertIsInstance(instance, PortisSDK)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortisSDK()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
