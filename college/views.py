from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


from .models import Course, Lesson, Subscription
from .permissions import IsModerator
from .serliazers import CourseSerializer, LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    управление курсом и проверка разрешений
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            return [permissions.IsAdminUser()]
        elif self.action in ["list", "retrieve", "update"]:
            return [IsModerator() or permissions.IsAuthenticated()]
        return super().get_permissions()

    def get_queryset(self):

        if (
            self.request.user.groups.filter(name="moderators").exists()
            or self.request.user.is_staff
        ):
            return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)


class LessonViewSet(viewsets.ModelViewSet):
    """
    управление уроком и проверка разрешений
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            return [permissions.IsAdminUser()]
        elif self.action in ["list", "retrieve", "update"]:
            return [IsModerator() or permissions.IsAuthenticated()]
        return super().get_permissions()

    def get_queryset(self):
        if (
            self.request.user.groups.filter(name="moderators").exists()
            or self.request.user.is_staff
        ):
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class SubscriptionView(APIView):
    """
    управление подписками и проверка на то есть ли она
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        course_id = request.data.get("course_id")
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course_item)
            message = "Подписка добавлена"

        return Response({"message": message})
