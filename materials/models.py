from django.db import models
from django.conf import settings


NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    picture = models.ImageField(upload_to='materials/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(max_length=200, verbose_name='описание')
    is_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель',
                                  **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    picture = models.ImageField(upload_to='materials/', verbose_name='картинка', **NULLABLE)
    description = models.TextField(max_length=200, verbose_name='описание')
    url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, verbose_name='курс')
    is_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель',
                                  **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
