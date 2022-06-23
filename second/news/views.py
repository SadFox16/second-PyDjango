from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

#функции для страниц

#ренедерим страницу index.html
def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories,
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id): #переход по категориям из сайдбара
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all() #получаем все категории
    category = Category.objects.get(pk=category_id) #получаем категорию из таблицы Category по primary key
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category': category}) #передаем полученные переменные в шаблон category.html
