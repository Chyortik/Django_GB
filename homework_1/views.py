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
                text-align: center;
            }
            table {
                margin: auto;
                width: 600px;
                text-align: center;
                border-collapse: collapse;
                border: 1px solid black;
            }
            th {
               border: 1px solid black;
            }
            td {
               border: 1px solid black;
            }
        </style>
    </head>
    <body>
        <h1>Приветствую на моем первом Django-сайте!</h1>
        <h5>Главная страница домашнего задания 1</h5>
        <table>
            
            <tr>
                <th>№ п/п</th>
                <th>Наименование</th>
                <th>Ссылки</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Игра орел и решка</td>
                <td>/eagle/кол-во бросков</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Игра игральная кость</td>
                <td>/cube/</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Игра случайное число</td>
                <td>/random_number/</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Показать результаты</td>
                <td>/show_elements/число</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Страница обо мне</td>
                <td>/about/</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Страница заказы пользователя (ДЗ №3)</td>
                <td>/user/ id пользователя</td>
            </tr>
            <tr>
                <td>7</td>
                <td>Страница заказы пользователя за определенный период (ДЗ №3)</td>
                <td>/user_sorted/ id пользователя/ кол-во дней (7, 30, 365)/</td>
            </tr>
            <tr>
                <td>8</td>
                <td>Главная страница ДЗ №4</td>
                <td>/hw_4/</td>
            </tr>
            <tr>
                <td>9</td>
                <td>Главная страница ДЗ №5</td>
                <td>/admin/ (доступ -> login: admin, pass: 1)</td>
            </tr>
        </table>



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