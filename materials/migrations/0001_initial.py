# Generated by Django 5.0.4 on 2024-04-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='картинка')),
                ('description', models.TextField(max_length=200, verbose_name='описание')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='картинка')),
                ('description', models.TextField(max_length=200, verbose_name='описание')),
                ('lessons', models.ManyToManyField(to='materials.lesson', verbose_name='Уроки для курса')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
