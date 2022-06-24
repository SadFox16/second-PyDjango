from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import News, Category
from .forms import NewsForm

#классы для страниц
class HomeNews(ListView): #возвращает список новостей, переопределяем аттрибуты, остальной рендер за нас делает класс
    model = News #получаем все данные из таблицы News
    template_name = 'news/home_news_list.html' #указываем какой шаблон использовать
    context_object_name= 'news'
    #extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs): #переопределяем метод для вывода title в имени вкладки
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self): #метод для фильтрования выводимых записей
        return News.objects.filter(is_published=True) #выводим только опубликованные записи


class NewsByCategory(ListView): #выводит статьи при выборе определенной категории
    model = News
    template_name ='news/home_news_list.html' #указываем какой шаблон использовать
    context_object_name = 'news'
    allow_empty = False #при несуществующей или пустой категории выводим 404

    def get_context_data(self, *, object_list=None, **kwargs): #переопределяем метод для вывода названия категории в имени вкладки
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self): #метод для фильтрования выводимых записей
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True) #выводим записи только выбранной категории

#функции для страниц
# def index(request): #функция заменена на класс HomeNews
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context=context)


def get_category(request, category_id): #переход по категориям из сайдбара
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id) #получаем категорию из таблицы Category по primary key
    return render(request, 'news/category.html', {'news': news, 'category': category}) #передаем полученные переменные в шаблон category.html


def view_news(request, news_id): #функция для просмотра новости
   # news_item = News.objects.get(pk=news_id) #получаем запрошенную новость по id
    news_item = get_object_or_404(News, pk=news_id) #выводим новость, иначе выдаем 404
    return render(request, 'news/view_news.html', {"news_item": news_item})

def add_news(request): #функция для формы добавления новости
    if request.method == 'POST':
        form = NewsForm(request.POST) #принимаем данные из формы
        if form.is_valid(): #проверка валидации
           #print(form.cleaned_data) #при прохождении создаем словарь cleaned_data у формы, куда записываются все прошедшие валидацию данные
            # news = News.objects.create(**form.cleaned_data) #добавляем запись в бд из формы
            news = form.save() #сохраняем данные из формы в news
            return redirect(news) #перенаправляем после добавления новости через форму на созданную новость
    else:
        form = NewsForm() #создаем пустую форму если данные пришли не POST-ом
    return render(request, 'news/add_news.html', {'form': form})
