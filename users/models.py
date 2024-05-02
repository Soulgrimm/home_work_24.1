from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import NULLABLE, Course


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='Страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(verbose_name='дата оплаты', **NULLABLE)
    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    amount = models.PositiveIntegerField(default=0, verbose_name='сумма оплаты')
    method = models.CharField(max_length=20, choices=(('card', 'Карта'), ('cash', 'Наличные')),
                              verbose_name='способ оплаты')

    session_id = models.CharField(max_length=255, verbose_name='id сессии', **NULLABLE)
    payment_link = models.URLField(max_length=400, verbose_name='ссылка на оплату', **NULLABLE)

    def __str__(self):
        return f"{self.user}: ({self.payment_course}) - {self.amount} ({self.payment_link})"

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
