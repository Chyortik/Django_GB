from django import forms
from .models import Product

"""
Задание №4.
Доработаем задачу про клиентов, заказы и товары из прошлого семинара.
Создайте форму для редактирования товаров в базе данных.
Измените модель продукта, добавьте поле для хранения фотографии продукта. 
Создайте форму, которая позволит сохранять фото.
"""


class ProductFormWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': f'введите название товара'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    number = forms.IntegerField(min_value=0)
    image = forms.ImageField()


class ProductChoiceForm(forms.Form):
    products = Product.objects.all()
    product_id = forms.ChoiceField(label='prod_id', choices=[(product.id, product.name) for product in products])


class ImageForm(forms.Form):
    image = forms.ImageField()
