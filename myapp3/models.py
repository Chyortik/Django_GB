from django.db import models


class Coin(models.Model):
    is_eagle = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сторона: {self.is_eagle}, Время: {self.create_at}'

    @staticmethod
    def counter(n: int):
        # coins = Coin.objects.all()[-1:-n - 1:-1]
        coins = Coin.objects.order_by('-create_at')[: n]
        coins_dict = {'орёл': 0, 'решка': 0}
        for coin in coins:
            if coin.is_eagle == 'орёл':
                coins_dict['орёл'] += 1
            else:
                coins_dict['решка'] += 1
        return coins_dict
        # return [str(coin) + '<br>' for coin in coins][-n::]


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.CharField(max_length=300)
    birthdate = models.DateField()

    def full_name(self):
        return f'{self.firstname} {self.lastname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

# Создайте модель Комментарий.
# Авторы могут добавлять комментарии к своим и чужим статьям. Т.е. у комментария может быть один автор.
# И комментарий относится к одной статье. У модели должны быть следующие поля
# автор
# статья
# комментарий
# дата создания
# дата изменения


class Comment(models.Model):
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    creates_at = models.DateField(auto_now_add=True)
    change_at = models.DateField(auto_now_add=True)
