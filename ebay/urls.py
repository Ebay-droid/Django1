from django.urls import path
from . import views

urlpatterns=[
  path('',views.index,name='index'),
  path('search/',views.search_results,name='search_results'),
  path('images/<id>',views.get_image_by_id, name ='get_image_by_id')
]