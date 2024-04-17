from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    num_of_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_num_of_lessons(self, instance):
        return instance.lesson_set.all().count()

    class Meta:
        model = Course
        fields = ('id', 'title', 'num_of_lessons')
