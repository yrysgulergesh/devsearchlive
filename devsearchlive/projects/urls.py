from importlib.resources import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projects),
    path('project/<str:pk>/', views.project), # int, slug
]

