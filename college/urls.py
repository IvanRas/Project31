"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from college.apps import CollegeConfig
from college.views import (
    CourseViewSet,
    LessonCreteAPIView,
    LessonDestroyAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
)

app_name = CollegeConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("", include(router.urls)),
    path("lesson/crete/", LessonCreteAPIView.as_view(), name="lesson_crete"),
    path("lesson/list/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/retriv/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retriv"),
    path("lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path(
        "lesson/destroy/<int:pk>/",
        LessonDestroyAPIView.as_view(),
        name="lesson_destroy",
    ),
]
