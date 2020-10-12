from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
  return render(request, 'index.html')


def search_results(request):
  
  if 'image' in request.GET and request.GET["IMAGE"]:
    search_term = request.GET("image")
    searched_images = Image.search_by_category(search_term)
    message = f"{search_term}"
    
    return render(request,"search.html", {'message':message,'images':searched_images})
  else:
    message = "Please input a valid term"
    return render(request,'search.html', {'message':message})
  
# def get_image_by_id(request,image_id):
  
  
  
    