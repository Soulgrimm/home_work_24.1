from rest_framework import viewsets, generics

from materials.models import Course, Lesson
from materials.permissions import IsStaff, IsAuthor, ViewPerm
from materials.serializers import CourseSerializer, LessonSerializer
from rest_framework.permissions import IsAuthenticated


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [ViewPerm]

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.is_author = self.request.user
        new_course.save()


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
