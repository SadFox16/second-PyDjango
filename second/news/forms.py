#файл с формами приложения news
from django import forms
from .models import News
import re
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm): #класс для описания вида формы добавления новости
    class Meta:
        model = News #с какой таблицей связываем форму
        #fields = '__all__' #какие поля нам нужны в форме
        fields = ['title', 'content', 'photo', 'is_published', 'category'] #какие поля нам нужны в форме
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    #пользовательский валидатор для поля title, чтобы заголовок не начинался с цифры
    def clean_title(self):
        title = self.cleaned_data['title'] #получаем title из словаря cleaned_data после стандартной валидации
        if re.match(r'\d', title): #ищем цифру в начале строки title
            raise ValidationError('Название не должно начинаться с цифры') #выбрасываем  exception при нахождении цифры в начале строки title
        return title
    
    # title = forms.CharField(max_length=150, label='Заголовок:', #название
    #                         widget=forms.TextInput(attrs={
    #                             "class": "form-control"
    #                         }))
    # content = forms.CharField(label='Текст:', required=False,  #текст
    #                           widget=forms.Textarea(attrs={
    #                               "class": "form-control",
    #                               "rows": 5
    #                           }))
    # is_published = forms.BooleanField(label='Публикация', initial=True) #опубликована ли
    # category = forms.ModelChoiceField(empty_label='Выберите категорию', label='Категория:', queryset=Category.objects.all(), #категория
    #                             widget=forms.Select(attrs={
    #                                 "class": "form-control"
    #                             }))

