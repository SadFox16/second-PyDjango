#файл с формами сайта
from django import forms
from .models import Category


class NewsForm(forms.Form): #класс для описания вида формы добавления новости
    title = forms.CharField(max_length=150, label='Заголовок:') #название
    content = forms.CharField(label='Текст:') #текст
    is_published = forms.BooleanField(label='Публикация:') #опубликована ли
    category = forms.ModelChoiceField(label='Категория:', queryset=Category.objects.all()) #категория

