from rest_framework import routers
from .api import TagsViewSet
from  Tags import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('tags/listAllTags/' , views.listed),
    path('tags/insertTags/', views.new_tags),
    path('tags/searchTags/<str:description>', views.tagsSearch),
    path('tags/updateTags/<str:description>',views.tagsChange), 
]

urlpatterns = format_suffix_patterns(urlpatterns)