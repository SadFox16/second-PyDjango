#файл с формами сайта
from django import forms
from .models import Category


class NewsForm(forms.Form): #класс для описания вида формы добавления новости
    title = forms.CharField(max_length=150, label='Заголовок:', #название
                            widget=forms.TextInput(attrs={
                                "class": "form-control"
                            }))
    content = forms.CharField(label='Текст:', required=False,  #текст
                              widget=forms.Textarea(attrs={
                                  "class": "form-control",
                                  "rows": 5
                              }))
    is_published = forms.BooleanField(label='Публикация', initial=True) #опубликована ли
    category = forms.ModelChoiceField(empty_label='Выберите категорию', label='Категория:', queryset=Category.objects.all(), #категория
                                widget=forms.Select(attrs={
                                    "class": "form-control"
                                }))

