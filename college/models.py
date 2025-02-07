from django.db import models
from django.conf import settings

# Create your models here.


class Course(models.Model):
    """
    класс курса - невание, описание, автор, фотография
    """

    title = models.CharField(max_length=150, verbose_name="название")
    preview = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="фото",
        help_text="Загрузити фотографию",
    )
    description = models.TextField(
        max_length=250, verbose_name="описание", help_text="Введите описание"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="courses",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Subscription(models.Model):
    """
    класс подписчика - имя, курс
    курс сязаный с классом курс
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="subscriptions", on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course, related_name="subscriptions", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ("user", "course")  # Обеспечивает уникальность подписки


class Lesson(models.Model):
    """
    класс урока - название, описание, автор, фотография, ссылка, подписчик
    пописчик сязаный с классом подписчик
    """

    title = models.CharField(max_length=150, verbose_name="название")
    description = models.TextField(
        max_length=250, verbose_name="описание", help_text="Введите описание"
    )
    preview = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="фото",
        help_text="Загрузити фотографию",
    )
    video_url = models.URLField(null=True, blank=True, verbose_name="Ссылка на видео")
    course = models.ForeignKey(
        Course, null=True, blank=True, related_name="lessons", on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="lessons",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    subs = models.ForeignKey(
        Subscription,
        null=True,
        blank=True,
        related_name="subscription",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
