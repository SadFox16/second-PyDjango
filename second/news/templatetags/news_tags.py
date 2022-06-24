# файл для пользовательских тегов
from django import template
from news.models import Category
from django.db.models import Count, F

register = template.Library()  # регистрируем пользовательский тег


@register.simple_tag(name='get_list_categories')  #декоратор для изменения поведения функции
def get_categories():  #функция для возврата категорий
    return Category.objects.all() #получаем список категорий


@register.inclusion_tag('news/list_categories.html')
def show_categories(): #inclusion тег
    #categories = Category.objects.all()
    #categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    categories = Category.objects.annotate(cnt=Count('news', filter=F('news__is_published'))).filter(cnt__gt=0) #выводим список категорий, считая только опубликованные записи
    return {"categories": categories}

