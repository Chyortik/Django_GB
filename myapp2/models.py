from django.db import models


# Семинар 2. Задание 1.
# Создайте модель для запоминания бросков монеты: орёл или решка. Также запоминайте время броска.


class Coin(models.Model):
    is_eagle = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сторона: {self.is_eagle}, Время: {self.create_at}'

    # Семинар 2. Задание 2.
    # Доработаем задачу 1.
    # Добавьте статический метод для статистики по n последним броскам монеты.
    # Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.

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


# Семинар 2. Задача 3.
# Создайте модель Автор. Модель должна содержать следующие поля:
# имя до 100 символов
# фамилия до 100 символов
# почта
# биография
# день рождения
# Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.CharField(max_length=300)
    birthdate = models.DateField()

    def full_name(self):
        return f'{self.firstname} {self.lastname}'


# Семинар 2. Задача 4.
# Создайте модель Статья (публикация). Авторы из прошлой задачи могут
# писать статьи. У статьи может быть только один автор. У статьи должны быть
# следующие обязательные поля:
# ○ заголовок статьи с максимальной длиной 200 символов
# ○ содержание статьи
# ○ дата публикации статьи
# ○ автор статьи с удалением связанных объектов при удалении автора
# ○ категория статьи с максимальной длиной 100 символов
# ○ количество просмотров статьи со значением по умолчанию 0
# ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
