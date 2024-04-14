from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter
from django.urls import path

from materials.views import CourseViewSet, LessonCreateView, LessonListView, LessonRetrieveView, LessonUpdateView, \
    LessonDestroyView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lesson/create/', LessonCreateView.as_view(), name='lesson-create'),
    path('lesson/list/', LessonListView.as_view(), name='lesson-list'),
    path('lesson/view/<int:pk>/', LessonRetrieveView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyView.as_view(), name='lesson-delete'),
] + router.urls
