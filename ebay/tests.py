from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class  LocationTestClass(TestCase):
  
  def setUp(self):
    self.mara = Location(name = 'Maasai mara')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.mara,Location))  
    
class CategoryTestClass(TestCase):
  def setUp(self):
    self.nature = Category(name = 'nature')    
    
  def test_instance(self):
    self.assertTrue(isinstance(self.nature,Category))  
    
class ArticleTestClass(TestCase):    