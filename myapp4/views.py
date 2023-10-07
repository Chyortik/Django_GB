from django.http import HttpRequest
from django.shortcuts import render
from random import choice, randint
from .forms import GamesForm, AddAuthorForm
from myapp4.models import Article, Author


def eagle(request: HttpRequest, count: int) -> render:
    # game_list = ['орёл', 'решка']
    # # response = random.choice(game_list)
    # # coin = Coin(is_eagle=response)
    # # coin.save()
    # # logger.info(f'Выпала сторона: {coin}')
    # # return HttpResponse(coin)
    # result = []
    # for i in range(count):
    #     response = random.choice(game_list)
    #     result.append(response)
    # context = {
    #     'result': result
    # }
    # return render(request, 'myapp4/index.html', context=context)
    res = {}
    for num in range(1, count + 1):
        res[num] = choice(('Орел', 'Решка'))
    context = {'title': 'All values Eagles', 'res': res}
    return render(request, template_name='myapp4/index.html', context=context)


# def show_elements(request, n: int):
#     return HttpResponse(f'{Coin.counter(n)}')


def cube(request, count: int) -> render:
    # cube_value = random.randint(1, 6)
    # logger.info(f'Выпало значение: {cube_value}')
    # return HttpResponse(cube_value)
    res = {}
    for num in range(1, count + 1):
        res[num] = choice(('Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть'))
    context = {'title': 'All values Cube', 'res': res}
    return render(request, template_name='myapp4/index.html', context=context)


def random_number(request, count: int) -> render:
    # r_num = random.randint(0, 100)
    # logger.info(f'Выпало число: {r_num}')
    # return HttpResponse(r_num)
    res = {}
    for num in range(1, count + 1):
        res[num] = randint(1, 100)
    context = {'title': 'All values random', 'res': res}
    return render(request, template_name='myapp4/index.html', context=context)


def game_choice(request):
    if request.method == "POST":
        form = GamesForm(request.POST)
        if form.is_valid():
            attempts = form.cleaned_data['attempts']
            game = form.cleaned_data['game']
            if game == 'E':
                return eagle(request, attempts)
            elif game == 'C':
                return cube(request, attempts)
            elif game == 'N':
                return random_number(request, attempts)
    else:
        form = GamesForm()

    context = {'form': form}
    return render(request, template_name='myapp4/game.html', context=context)


def get_articles(request, author_id: int):
    author = Author.objects.get(id=author_id)
    articles = Article.objects.filter(author_id=author.id)
    context = {
        'articles': articles
    }
    return render(request, 'myapp4/base.html', context=context)


def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        h1 = 'Fill fields'
        if form.is_valid():
            author = Author.objects.create(**form.cleaned_data)
            author.save()
            return get_articles(request, author_id=author.pk)

    else:
        form = AddAuthorForm()
        h1 = 'Добавление автора'
    context = {'h1': h1, 'form': form}
    return render(request, template_name='myapp4/add_author.html', context=context)
