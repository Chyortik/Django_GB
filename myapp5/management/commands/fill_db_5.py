from django.core.management.base import BaseCommand
from myapp5.models import Author, Article


class Command(BaseCommand):
    help = 'Create fake authors'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Author_ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            author = Author(firstname=f'firstname{i}', lastname=f'lastname{i}',
                            email=f'email{i}@mail.ru', biography=f'biography{i}',
                            birthdate=f'2000-01-01')
            author.save()
            for j in range(1, count + 1):
                article = Article(title=f'title{j}', description=f'description{j}',
                                  author_id=author, category=f'category{j}')
                article.save()
