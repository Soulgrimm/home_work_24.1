import datetime

from celery import shared_task
from config import settings
from django.core.mail import send_mail

from materials.models import Subscription
from users.models import User


@shared_task
def update_course(course_id):
    course_subscriptions = Subscription.objects.filter(course_id=course_id)
    for subscription in course_subscriptions:
        if subscription.sign_subs:
            send_mail(
                subject="Курс обновлен",
                message="Курс на который вы подписаны был обновлен",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[subscription.user.email],
                fail_silently=False
            )
            print("Сообщение отправлено")


@shared_task
def check_activity():
    month_inactivity = datetime.now() - datetime.timedelta(days=30)
    users = User.objects.filter(is_active=True, is_staff=False, is_superuser=False, last_login__gte=month_inactivity)
    for user in users:
        user.is_active = False
        user.save()
