from django.http import HttpResponse
import logging
from datetime import datetime

from django.shortcuts import render

from myapp3.models import Article, Author, Comment

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'text': 'Задача 1. Изменяем задачу 8 из семинара 1 с выводом двух html страниц: главной и о себе. '
                'Перенесите вёрстку в шаблоны. Представления должны пробрасывать полезную'
                ' информацию в шаблон через контекст.',
        'text_2': ' Задача 2. Доработаем задачу 1. Выделите общий код шаблонов и создайте родительский шаблон'
                ' base.html. Внесите правки в дочерние шаблоны.'
    }
    # logger.info(f'посещение страницы index в: {datetime.now()}')
    return render(request, 'myapp3/index.html', context=context)


def about(request):
    context = {
        'text': 'Привет! Мой ник на Github Chortyk'
    }

    # logger.info(f'посещение страницы about в: {datetime.now()}')
    return render(request, 'myapp3/about.html', context=context)


def get_articles(request, author_id: int):
    author = Author.objects.get(id=author_id)
    articles = Article.objects.filter(author_id=author.id)
    context = {
        'articles': articles
    }
    return render(request, 'myapp3/about.html', context=context)


def detail_article(request, article_id: int):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by('-change_at')
    article.count_views += 1
    article.save()
    context = {
        'article': article,
        'comments': comments,
    }
    return render(request, 'myapp3/detail.html', context=context)
