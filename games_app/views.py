import random

from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def eagle(request):
    game_list = ['орёл', 'решка']
    response = random.choice(game_list)
    logger.info(f'Выпала сторона: {response}')
    return HttpResponse(response)


def cube(request):
    cube_value = random.randint(1, 6)
    logger.info(f'Выпало значение: {cube_value}')
    return HttpResponse(cube_value)


def random_number(request):
    r_num = random.randint(0, 100)
    logger.info(f'Выпало число: {r_num}')
    return HttpResponse(r_num)
