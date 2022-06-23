# файл для пользовательских тегов
from django import template
from news.models import Category

register = template.Library()  # регистрируем пользовательский тег


@register.simple_tag(name='get_list_categories')  #декоратор для изменения поведения функции
def get_categories():  #функция для возврата категорий
    return Category.objects.all() #получаем список категорий


@register.inclusion_tag('news/list_categories.html')
def show_categories(): #inclusion тег
    categories = Category.objects.all()
    return {"categories": categories}