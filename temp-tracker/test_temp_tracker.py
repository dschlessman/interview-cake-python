"""test_temp_tracker

Unit tests for the temp_tracker module

Test fixtures:
    TempTrackerNoDataCase: tests exceptions when no data input and statistics requested
    TempTrackerMixedDataTestCase: test data has integers, floats, and negative temperatures
    TempTrackerAllNegativeDataCase: test data is all negative temperatures
"""
from temp_tracker import TempTracker
import unittest

class TempTrackerNoDataCase(unittest.TestCase):
    def setUp(self):
        self.tracker = TempTracker()
    
    def test_get_max(self):
        with self.assertRaises(LookupError):
            self.tracker.get_max()
    
    def test_get_min(self):
        with self.assertRaises(LookupError):
            self.tracker.get_min()
    
    def test_get_mean(self):
        with self.assertRaises(LookupError):
            self.tracker.get_mean()

    def test_get_mode(self):
        with self.assertRaises(LookupError):
            self.tracker.get_mode()

class TempTrackerMixedDataTestCase(unittest.TestCase):
    def setUp(self):
        self.tracker = TempTracker()
        test_data = [1.4,1.4,1.4,3,4,5,5,6,-4]
        for temp in test_data:
            self.tracker.insert(temp)
    
    def test_get_max(self):
        self.assertEqual(self.tracker.get_max(), 6.0)
    
    def test_get_min(self):
        self.assertEqual(self.tracker.get_min(), -4)
    
    def test_get_mean(self):
        self.assertAlmostEqual(self.tracker.get_mean(), 2.57777777777777)

    def test_get_mode(self):
        self.assertEqual(self.tracker.get_mode(), 1.4)

class TempTrackerAllNegativeDataCase(unittest.TestCase):    
    def setUp(self):
        self.tracker = TempTracker()
        test_data = [-3,-2.3,-5,-5,-4,-4]
        for temp in test_data:
            self.tracker.insert(temp)
    
    def test_get_max(self):
        self.assertEqual(self.tracker.get_max(), -2.3)
    
    def test_get_min(self):
        self.assertEqual(self.tracker.get_min(), -5)
    
    def test_get_mean(self):
        self.assertAlmostEqual(self.tracker.get_mean(), -3.88333333)

    def test_get_mode(self):
        self.assertIn(self.tracker.get_mode(), [-4,-5])


if __name__ == "__main__":
    unittest.main()