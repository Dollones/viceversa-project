from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('reversed/', views.reverse, name='reverse'),
]
