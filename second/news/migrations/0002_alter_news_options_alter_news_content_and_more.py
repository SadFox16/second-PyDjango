# Generated by Django 4.0.5 on 2022-06-22 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['created_date'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время публикации'),
        ),
        migrations.AlterField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Время редактирования'),
        ),
    ]
