# Generated by Django 5.1.4 on 2025-01-02 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="название")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузити фотографию",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="фото",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание",
                        max_length=250,
                        verbose_name="описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "курс",
                "verbose_name_plural": "курсы",
            },
        ),
        migrations.CreateModel(
            name="Lesson",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="название")),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание",
                        max_length=250,
                        verbose_name="описание",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузити фотографию",
                        null=True,
                        upload_to="product/photo",
                        verbose_name="фото",
                    ),
                ),
                ("link_to_video", models.TextField(verbose_name="ссылка на видео")),
            ],
            options={
                "verbose_name": "урок",
                "verbose_name_plural": "уроки",
            },
        ),
    ]
