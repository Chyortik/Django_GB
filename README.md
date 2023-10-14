# Урок 1. Первое Знакомство с Django

Задание [code](./homework_1/views.py)
* Создайте пару представлений в вашем первом приложении: — главная — о себе.
* Внутри каждого представления должна быть переменная html — многострочный текст 
с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
* Сохраняйте в логи данные о посещении страниц. 


# Урок 2. Django ORM и связи
Задание
* Создайте три модели Django: клиент, товар и заказ [code](./homework_2/models.py)

Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа

* Допишите несколько функций CRUD для работы с
моделями по желанию. Что по вашему мнению актуально в
такой базе данных [code](./homework_2/management/commands)



# Урок 3. Шаблоны, классы и формы
Задание
Продолжаем работать с товарами и заказами.
* Доработаем задачу 8 из прошлого семинара про клиентов, товары и заказы.
Создайте шаблон для вывода всех заказов клиента и списком товаров внутри
каждого заказа. Подготовьте необходимый [маршрут](./homework_3/urls.py) и [представление](./homework_3/models.py)
* Создайте [шаблон](./homework_3/templates/homework_3/user_all_product.html), который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
— за последние 7 дней (неделю)
— за последние 30 дней (месяц)
— за последние 365 дней (год)

Товары в списке не должны повторяться.


# Урок 4. Работа с пользователями и права в Django. Оптимизация проекта
Задание [homework_4](./homework_4/)  

**Создана папка media в проекте** [media](./media/)

Доработаем задачу про клиентов, заказы и товары из прошлого семинара.
* Создайте форму для редактирования товаров в базе данных.
* Измените модель продукта, добавьте поле для хранения фотографии продукта. 
* Создайте форму, которая позволит сохранять фото.
  


# Урок 5. Развертывание Django проекта. Тестирование проекта
Задание [homework_5](./homework_5/). 
Настройте под свои нужды вывод информации о клиентах, товарах и заказах на страницах вывода
информации об объекте и вывода списка объектов [code](./homework_5/admin.py).



# Урок 6. Развёртывание проекта
Задание
Настроить работу проекта на сервере.
база данных - django_sems
pass - 1144WWee