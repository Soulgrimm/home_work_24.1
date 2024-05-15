from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.response import Response

from materials.models import Course, Lesson, Subscription
from materials.paginators import AllPaginator
from materials.permissions import IsStaff, IsAuthor
from materials.serializers import CourseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from materials.tasks import update_course


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = []
    pagination_class = AllPaginator

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.is_author = self.request.user
        new_course.save()

    def perform_update(self, serializer):
        course_update_notification = serializer.save()
        update_course.delay(course_update_notification.id)
        course_update_notification.save()

    def has_permission(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, ~IsStaff]
        elif self.action in ['retrieve', 'update', 'list']:
            permission_classes = [IsAuthenticated, IsAuthor | IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsAuthor]
        return [permission() for permission in permission_classes]


class LessonCreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsStaff]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.is_author = self.request.user
        new_lesson.save()


class LessonListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor | IsStaff]
    pagination_class = AllPaginator


class LessonRetrieveView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor | IsStaff]


class LessonUpdateView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor | IsStaff]


class LessonDestroyView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor]


class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data["course"]
        course_item = get_object_or_404(Course, id=course_id)
        subs_item, created = Subscription.objects.update_or_create(course=course_item, user=user)
        print(created)

        if created:
            subs_item.sign_subs = True
            subs_item.save()
            message = 'подписка добавлена'

        else:
            subs_item.sign_subs = False
            subs_item.save()
            message = 'подписка удалена'

        return Response({"message": message})
