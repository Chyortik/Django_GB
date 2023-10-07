from django.urls import path
from . import views

urlpatterns = [
    path('eagle4/<int:count>', views.eagle, name='eagle'),
    path('cube4/', views.cube, name='cube'),
    path('random_number4/', views.random_number, name='random_number'),
    path('games/', views.game_choice, name='games'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_article/<int:author_id>', views.get_articles, name='articles'),
]
