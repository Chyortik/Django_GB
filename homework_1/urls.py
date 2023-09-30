from django.urls import path
from . import views

urlpatterns = [
    path('main_page/', views.index, name='main_page'),
    path('about/', views.about, name='about_page'),
]