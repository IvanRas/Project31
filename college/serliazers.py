from rest_framework import serializers

from college.models import Course, Lesson
from .validators import TitleValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [TitleValidator(field='title')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

    @staticmethod
    def get_lesson_count(obj):
        return obj.lessons.count()
