from django.test import TestCase
from ..models import Posts
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpData: Run once to set up non-modified data for every")
        pass
    
    
    def setUp(self):
        print("SetUp : Run once for each time clean data")
        pass
    
    
    def test_false_is_false(self):
        print("Method: test_false_is_false")
        self.assertFalse(False)
    
    
    def test_false_is_true(self):
        print("Method: test_false_is_true")
        self.assertTrue(True)
        
        
    # def test_one_plus_one_equals_two(self):
    #     print("Method:test_one_plus_one_equals_two")
    #     post=Posts()
    #     self.assertEqual(1+1,2)
        
    def test_compare_equal(self):
        print("Are they equal?")
        post = Posts()
        self.assertEqual(Posts.get_number(), )
  