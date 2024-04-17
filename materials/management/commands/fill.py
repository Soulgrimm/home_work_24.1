import datetime

from django.core.management import BaseCommand

from materials.models import Course
from users.models import Payments, User


class Command(BaseCommand):

    def handle(self, *args, **options):
        Payments.objects.all().delete()

        user1, created = User.objects.get_or_create(email='test@sky.pro')
        user2, created = User.objects.get_or_create(email='GromovPR@yandex.ru')

        course1, created = Course.objects.get_or_create(title='Курс_1')
        course2, created = Course.objects.get_or_create(title='Курс_2')

        payment_list = [
            {'user': user1, 'payment_date': datetime.datetime.now().date(), 'payment_course': course1, 'amount': 10000,
             'method': 'card'},
            {'user': user2, 'payment_date': datetime.datetime.now().date(), 'payment_course': course2, 'amount': 20000,
             'method': 'cash'},
        ]

        payment_for_create = []

        for payment_item in payment_list:
            payment_for_create.append(Payments(**payment_item))

        Payments.objects.bulk_create(payment_for_create)
