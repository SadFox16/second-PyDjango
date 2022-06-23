from django.db import models
from django.urls import reverse

#Таблицы для news(после каждого изменения не забывать делать миграции)


class Category(models.Model): #Таблица категорий(первичная таблица)
    title = models.CharField(max_length=150, db_index=True, verbose_name='Заголовок') #db_index - индексация поля, ускорение поиска

    def get_absolute_url(self): #метод, указывающий на конкретную категорию для построения ссылки
        return reverse('category', kwargs={"category_id": self.pk}) #передаем в reverse имя маршрута и параметр для его построения


    def __str__(self): #строковое представление объекта для красивого отображения на странице
        return self.title

    class Meta: #подкласс для мета-описания таблицы
        verbose_name = 'Категория' #именование таблицы в единственном числе
        verbose_name_plural = 'Категории' #именование таблицы во множественном числе
        ordering = ['title'] #сортировка записей в таблице


class News(models.Model): #таблица для новостей(вторичная таблица)
    title = models.CharField(max_length=150, verbose_name = 'Заголовок') #заголовок новости
    content = models.TextField(blank=True, verbose_name = 'Текст') #текст новости
    created_date = models.DateTimeField(auto_now_add=True, verbose_name = 'Время публикации') #дата и время создания
    updated_date = models.DateTimeField(auto_now=True, verbose_name = 'Время редактирования') #дата и время изменения
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name = 'Фото') #изображение новости
    is_published = models.BooleanField(default=True, verbose_name = 'Публикация') #опубликована ли запись
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория') #foreign key для связи таблиц News и Category(ссылка на таблицу для связи, защита от удаления связанных данных, ...)

    def get_absolute_url(self): #метод, указывающий на конкретную категорию для построения ссылки
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self): #строковое представление объекта для красивого отображения на странице
        return self.title

    class Meta: #подкласс для мета-описания таблицы
        verbose_name = 'Новость' #именование таблицы в единственном числе
        verbose_name_plural = 'Новости' # именование таблицы во множественном числе
        ordering = ['created_date'] #сортировка записей в таблице


