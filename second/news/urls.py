from django.urls import path

from .views import *

urlpatterns = [ #список url-ов(маршрутов) для новостей
    #предыдущие маршруты, заменены после замены функций на классы
    #path('', index, name='home'), #главная
    #path('category/<int:category_id>/', get_category, name='category'), #категории
    #path('news/<int:news_id>/', view_news, name='view_news'), #страница просмотра новости
    #path('news/add-news', add_news, name='add_news'), #страница с формой добавления новости
    path('register/', register, name='register'), #регистрация
    path('login/', login, name='login'), #авторизация
    path('', HomeNews.as_view(), name='home'),  #главная
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'), #категории
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'), #страница просмотра новости
    path('news/add-news', CreateNews.as_view(), name='add_news'), #страница с формой добавления новости
]