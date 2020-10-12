from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class  LocationTestClass(TestCase):
  
  def setUp(self):
    self.mara = Location(name = 'Maasai mara')
    
  def test_instance(self):
    self.assertTrue(isinstance(self.mara,Location))  
    
  def test_save_method(self):
    self.mara.save_location()
    location = Location.objects.all()
    self.assertTrue(len(location) > 0)
      
    
class CategoryTestClass(TestCase):
  def setUp(self):
    self.nature = Category(name = 'Nature')    
    
  def test_instance(self):
    self.assertTrue(isinstance(self.nature,Category)) 
    
  def test_save_category(self):
    self.nature.save_category()
    category = Category.objects.all()
    self.assertTrue(len(category) >0)
    
class ImageTestClass(TestCase):    
  def setUp(self):
    
    self.mara = Location(name = 'Maasai mara')
    self.mara.save_location()
    self.nature = Category(name = 'Nature')
    self.nature.save_category()
    
    
    