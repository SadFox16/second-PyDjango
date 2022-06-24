from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import News, Category
from .forms import NewsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

#классы для страниц
class HomeNews(ListView): #возвращает список новостей, переопределяем аттрибуты, остальной рендер за нас делает класс
    model = News #получаем все данные из таблицы News
    template_name = 'news/home_news_list.html' #указываем какой шаблон использовать
    context_object_name = 'news'
    mixin_prop = 'hello world'
    paginate_by = 10
    #extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs): #переопределяем метод для вывода title в имени вкладки
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        #context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self): #метод для фильтрования выводимых записей
        return News.objects.filter(is_published=True).select_related('category') #выводим только опубликованные записи


class NewsByCategory(ListView): #выводит статьи при выборе определенной категории
    model = News
    template_name ='news/home_news_list.html' #указываем какой шаблон использовать
    context_object_name = 'news'
    allow_empty = False #при несуществующей или пустой категории выводим 404
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs): #переопределяем метод для вывода названия категории в имени вкладки
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self): #метод для фильтрования выводимых записей
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category') #выводим записи только выбранной категории


class ViewNews(DetailView): #класс для страницы просмотра новости
    model = News #получаем все данные из таблицы News
    #template_name = 'news/news_detail.html' #указываем какой шаблон использовать
    #pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView): #класс для формы создания новости
    form_class = NewsForm #связываем класс с классом формы
    template_name = 'news/add_news.html' #указываем какой шаблон использовать
    success_url = reverse_lazy('home') #редирект после добавления новой новости
    #login_url = '/admin/'
    raise_exception = True #ограничиваем доступ к форме добавления новости


#функции для страниц
# def index(request): #функция заменена на класс HomeNews
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context=context)


# def get_category(request, category_id): #переход по категориям из сайдбара
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id) #получаем категорию из таблицы Category по primary key
#     return render(request, 'news/category.html', {'news': news, 'category': category}) #передаем полученные переменные в шаблон category.html


# def view_news(request, news_id): #функция для просмотра новости, заменена на класс ViewNews
#    # news_item = News.objects.get(pk=news_id) #получаем запрошенную новость по id
#     news_item = get_object_or_404(News, pk=news_id) #выводим новость, иначе выдаем 404
#     return render(request, 'news/view_news.html', {"news_item": news_item})

# def add_news(request): #функция для формы добавления новости, заменена на класс CreateView
#     if request.method == 'POST':
#         form = NewsForm(request.POST) #принимаем данные из формы
#         if form.is_valid(): #проверка валидации
#            #print(form.cleaned_data) #при прохождении создаем словарь cleaned_data у формы, куда записываются все прошедшие валидацию данные
#             # news = News.objects.create(**form.cleaned_data) #добавляем запись в бд из формы
#             news = form.save() #сохраняем данные из формы в news
#             return redirect(news) #перенаправляем после добавления новости через форму на созданную новость
#     else:
#         form = NewsForm() #создаем пустую форму если данные пришли не POST-ом
#     return render(request, 'news/add_news.html', {'form': form})
