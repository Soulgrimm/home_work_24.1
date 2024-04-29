from rest_framework import serializers

from materials.models import Course, Lesson, Subscription
from materials.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='url')]


class CourseSerializer(serializers.ModelSerializer):
    num_of_lessons = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    def get_num_of_lessons(self, instance):
        return instance.lesson_set.all().count()

    def get_subscription(self, instance):
        user = self.context['request'].user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, course=instance).first()
            return subscription.sign_subs

    class Meta:
        model = Course
        fields = ('id', 'title', 'num_of_lessons')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
