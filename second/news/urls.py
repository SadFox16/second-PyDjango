from django.urls import path

from .views import *

urlpatterns = [ #список url-ов(маршрутов) для новостей
    path('', index, name='home'), #главная
    path('category/<int:category_id>/', get_category, name='category'), #категории
    path('news/<int:news_id>/', view_news, name='view_news'), #страница просмотра новости
    path('news/add-news', add_news, name='add_news'), #страница с формой добавления новости
]