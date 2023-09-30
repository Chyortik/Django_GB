from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 24px;
            }

            h1 {
                color: #256ab6;
                text-align: center;
            }
            h2 {
                color: #32a54f
            }
            p {
                color: #a12a8d;
            }
            h5 {
                color: #b66a25;
            }
        </style>
    </head>
    <body>
        <h1>Приветствую на моем первом Django-сайте!</h1>

        <h2>О сайте</h2>
        <p>Сайт разработан с помощью Django, мощного фреймворка для
         создания веб-приложений на языке Python. Здесь можно создавать и отображать
          различные страницы и данные в удобном формате.</p>

        <h2>Обо мне</h2>
        <p>Привет, меня зовут Chortyk. Я начинающий front-end разработчик.
         Мне нравится создавать удобные и красивые веб-сайты.
          Мои навыки включают умение работать с HTML, CSS, SQL, а также Python и Django.</p>

        <footer>
            <p>Свяжитесь со мной: </p>
            <p>sss222@mail.ru</p>
            <p>+7-900-000-00-00</p>
        </footer>
    </body>
    </html>
    """
    logger.info(f'посещение страницы index в: {datetime.now()}')
    return HttpResponse(html)


def about(request):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обо мне</title>
</head>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.5;
                margin: 0;
                padding: 24px;
            }

            h1 {
                color: #256ab6;
                text-align: center;
            }
            h2 {
                color: #32a54f
            }
            p {
                color: #a12a8d;
            }
            h5 {
                color: #b66a25;
            }
        </style>
<body>
    <header>
        <h1>Привет! Мой ник на Github Chortyk</h1>
    </header>

    <main>
        <section>
            <h2>Опыт работы</h2>
            <ul>
                <li>Место работы 1</li>
                <li>Место работы 2</li>
                <li>Место работы 3</li>
            </ul>
        </section>

        <section>
            <h2>Образование</h2>
            <ul>
                <li>Университет 1</li>
                <li>Курсы 1</li>
                <li>Курсы 2</li>
            </ul>
        </section>

        <section>
            <h2>Навыки</h2>
            <ul>
                <li>Навык 1</li>
                <li>Навык 2</li>
                <li>Навык 3</li>
            </ul>
        </section>
    </main>

    <footer>
            <p>Свяжитесь со мной:</p>
            <h5>sss222@mail.ru</h5>
            <h5>+7-900-000-00-00</h5>
    </footer>
</body>
</html>
"""
    logger.info(f'посещение страницы about в: {datetime.now()}')
    return HttpResponse(html)