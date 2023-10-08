from django.contrib import admin
from .models import Article, Author, Comment, Coin

admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Coin)
