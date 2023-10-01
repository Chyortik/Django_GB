import random

from django.http import HttpResponse
import logging

from django.shortcuts import render

from myapp2.models import Coin

logger = logging.getLogger(__name__)


def eagle(request, count: int):
    game_list = ['орёл', 'решка']
    # response = random.choice(game_list)
    # coin = Coin(is_eagle=response)
    # coin.save()
    # logger.info(f'Выпала сторона: {coin}')
    # return HttpResponse(coin)
    result = []
    for i in range(count):
        response = random.choice(game_list)
        result.append(response)
    context = {
        'result': result
    }
    return render(request, 'myapp3/index.html', context=context)


def show_elements(request, n: int):
    return HttpResponse(f'{Coin.counter(n)}')


def cube(request):
    cube_value = random.randint(1, 6)
    logger.info(f'Выпало значение: {cube_value}')
    return HttpResponse(cube_value)


def random_number(request):
    r_num = random.randint(0, 100)
    logger.info(f'Выпало число: {r_num}')
    return HttpResponse(r_num)
