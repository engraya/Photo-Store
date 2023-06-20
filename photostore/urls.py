from django.urls import path
# this imports all the views from the views.py
from . import views

urlpatterns = [
    # this is the home url
    path('', views.home, name='home'),
    # this is the single book url
    path('detail/<str:id>/', views.detail, name='detail'),
    # this is the add book url
    path('add/', views.add, name='add'),
        # this is the delete book url
    path('update/<str:id>/', views.update, name='update'),
    # this is the delete book url
    path('delete/<str:id>/', views.delete, name='delete'),


]