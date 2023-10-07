from django import forms
from .models import Author, Article

"""
Доработаем задачу про броски монеты, игральной кости и случайного числа.
Создайте форму, которая предлагает выбрать: монета, кости, числа.
Второе поле предлагает указать количество попыток от 1 до 64.
"""

GAMES = [('E', 'eagle'), ('C', 'cube'), ('N', 'random_number')]


class GamesForm(forms.Form):
    attempts = forms.IntegerField(min_value=1, max_value=64)
    game = forms.ChoiceField(choices=GAMES)


"""
Продолжаем работу с авторами, статьями и комментариями.
Создайте форму для добавления нового автора в базу данных.
Используйте ранее созданную модель Author.
Аналогично автору создайте форму добавления новой статьи.
Автор статьи должен выбираться из списка (все доступные в базе данных авторы).
"""


class AddAuthorForm(forms.ModelForm):
    biography = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'your biography'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta():
        model = Author
        fields = ['firstname', 'lastname', 'email', 'biography', 'birthdate']

# class AddArticleForm(forms.ModelForm):
#     class Meta():
#         model = Article
#         fields = ['title', 'description', 'created_at', 'author_id',
#                   'category', count_views = models.IntegerField(default=0)
#     is_published = models.BooleanField(default=False)
