# Generated by Django 5.0.4 on 2024-05-01 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_payments'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='payment_link',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payments',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id сессии'),
        ),
    ]
