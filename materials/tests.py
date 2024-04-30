from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from materials.models import Lesson, Course, Subscription
from users.models import User


class AllTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.pro', is_active=True, is_superuser=True, is_staff=True)
        self.user.set_password('qqqwww111222')

        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):
        data = {"title": "test", "description": "test", "url": "https://www.youtube.com/test"}
        response = self.client.post(reverse('materials:lesson-create'), data=data)
        print(response)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_lesson(self):
        response = self.client.get(reverse('materials:lesson-list'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        lesson = Lesson.objects.create(is_author=self.user,
                                       title='test lesson',
                                       description='test content'
                                       )
        update_data = {
            "title": "update",
            "url": "https://www.youtube.com/test2"
        }

        response = self.client.patch(reverse('materials:lesson-update', args=[lesson.id]), update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_lesson(self):
        lesson = Lesson.objects.create(is_author=self.user,
                                       title='test lesson',
                                       description='test content',
                                       url="https://www.youtube.com/test")

        response = self.client.delete(reverse('materials:lesson-delete', args=[lesson.id]))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_subscribe_course(self):
        course_item = Course.objects.create(is_author=self.user,
                                            title='test course',
                                            description='test content')

        subs = {
            "user": self.user,
            "course": course_item.id
        }

        response = self.client.post(reverse('materials:subscription'), data=subs)
        self.assertEqual(response.data['message'], 'подписка добавлена')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unsubscribe_course(self):
        course_item = Course.objects.create(is_author=self.user,
                                            title='test course',
                                            description='test content')

        subs = {
            "user": self.user,
            "course": course_item.id,
        }

        self.client.post(reverse('materials:subscription'), data=subs)
        response = self.client.post(reverse('materials:subscription'), data=subs)
        self.assertEqual(response.data['message'], 'подписка удалена')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
