from django.db import models

# Create your models here.

  
class Location(models.Model): 
  name = models.CharField(max_length=30)
  
  def save_location(self):
    self.save()
    
  def delete_location(self):
    self.delete()   
    
    
class Category(models.Model):
  name = models.CharField(max_length=10)  
  
  def save_category(self):
    self.save()
    
  def delete_category(self):
    self.delete()    
    
    
class  Image(models.Model):
  image = models.ImageField(upload_to = 'images/')
  name= models.CharField(max_length =10)
  description= models.TextField()
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  
  def save_image(self):
    self.save()
    
  def delete_image(self):
    self.delete()  
      
  @classmethod
  def search_by_name(cls, search_term):
    image = cls.objects.filter(name=search_term)
    return image    