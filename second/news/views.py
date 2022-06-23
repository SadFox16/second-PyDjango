from django.shortcuts import render, get_object_or_404
from .models import News, Category
from .forms import NewsForm

#функции для страниц

#ренедерим страницу index.html
def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id): #переход по категориям из сайдбара
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id) #получаем категорию из таблицы Category по primary key
    return render(request, 'news/category.html', {'news': news, 'category': category}) #передаем полученные переменные в шаблон category.html


def view_news(request, news_id): #функция для просмотра новости
   # news_item = News.objects.get(pk=news_id) #получаем запрошенную новость по id
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {"news_item": news_item})

def add_news(request): #функция для формы добавления новости
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})