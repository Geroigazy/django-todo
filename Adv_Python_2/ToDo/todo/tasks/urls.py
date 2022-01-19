from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="list" ),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('deleteall/', views.deleteall, name="deleteall")
]