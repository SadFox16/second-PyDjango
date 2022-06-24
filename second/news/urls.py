from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [ #список url-ов(маршрутов) для новостей
    #предыдущие маршруты, заменены после замены функций на классы
    #path('', index, name='home'), #главная
    #path('category/<int:category_id>/', get_category, name='category'), #категории
    #path('news/<int:news_id>/', view_news, name='view_news'), #страница просмотра новости
    #path('news/add-news', add_news, name='add_news'), #страница с формой добавления новости
    path('register/', register, name='register'), #регистрация
    path('login/', user_login, name='login'), #авторизация
    path('logout/', user_logout, name='logout'), #выход
    #path('', cache_page(60)(HomeNews.as_view()), name='home'),  #главная
    path('', HomeNews.as_view(), name='home'),  #главная
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'), #категории
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'), #страница просмотра новости
    path('news/add-news', CreateNews.as_view(), name='add_news'), #страница с формой добавления новости
]