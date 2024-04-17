from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    picture = models.ImageField(upload_to='materials/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(max_length=200, verbose_name='описание')
    url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    picture = models.ImageField(upload_to='materials/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(max_length=200, verbose_name='описание')
    lessons = models.ManyToManyField(Lesson, verbose_name='Уроки для курса')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"