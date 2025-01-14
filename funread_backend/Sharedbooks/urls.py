from rest_framework import routers
from  Sharedbooks import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import SharedBooksViewSet

urlpatterns = [
    path('sharedbooks/listAllSharedBooks/' , views.listed),
    path('sharedbooks/searchSharedBooks/', views.search),
    path('sharedbooks/insertnewSharedBooks/', views.add_new),
    path('sharedbooks/deleteSharedBooks/', views.delete),
    path('sharedbooks/updateSharedBooks/',views.update),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)