from django.urls import path

from .views import *

urlpatterns = [ #список url-ов(маршрутов) для новостей
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
]