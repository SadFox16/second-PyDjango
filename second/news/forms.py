#файл с формами сайта
from django import forms
from .models import Category


class NewsForm(forms.Form): #класс для описания вида формы добавления новости
    title = forms.CharField(max_length=150), #название
    content = forms.CharField(), #текст
    is_published = forms.BooleanField(), #опубликована ли
    category = forms.ModelChoiceField(queryset=Category.objects.all()), #категория

