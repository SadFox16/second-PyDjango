from django.contrib import admin
from .models import News, Category
from django.utils.safestring import mark_safe

class NewsAdmin(admin.ModelAdmin): #класс для редактирования внешнего вида таблицы News в админке
    list_display = ('id', 'title', 'created_date', 'category', 'updated_date', 'is_published') #что отображать в таблице на странице админки
    list_display_links = ('id', 'title') #какие поля записей станут ссылками
    search_fields = ('title', 'content') #по каким полям вести поиск
    list_editable = ('is_published', ) #изменяемое поле
    list_filter = ('is_published', 'category') #по каким полям доступно фильтрование
    fields = ('title', 'category', 'content', 'photo', 'created_date', 'updated_date', 'is_published', 'views_count')
    readonly_fields = ('views_count', 'created_date', 'updated_date')
    save_on_top = True

class CategoryAdmin(admin.ModelAdmin):  #класс для редактирования внешнего вида таблицы Category в админке
        list_display = ('id', 'title')  #что отображать в таблице на странице админки
        list_display_links = ('id', 'title')  #какие поля записей станут ссылками
        search_fields = ('title',)  #по каким полям вести поиск


#superuser: admin 12345
admin.site.register(News, NewsAdmin) #регистрируем таблицу News и класс редактирования
admin.site.register(Category, CategoryAdmin) #регистрируем таблицу Category и класс редактирования

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'


