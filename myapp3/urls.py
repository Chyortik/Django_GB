from django.urls import path
from myapp3 import views

urlpatterns = [
    path('app3/', views.index, name='index'),
    path('about3/', views.about, name='about'),
    path('articles/<int:author_id>', views.get_articles, name='articles'),
    path('detail/<int:article_id>', views.detail_article, name='detail_article'),
]
