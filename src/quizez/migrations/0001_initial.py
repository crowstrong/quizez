# Generated by Django 4.1.1 on 2022-09-21 17:58

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("create_datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                ("name", models.CharField(max_length=512)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Quiz",
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
                ("create_datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                ("title", models.CharField(max_length=128)),
                (
                    "description",
                    models.TextField(blank=True, max_length=1024, null=True),
                ),
                (
                    "level",
                    models.PositiveSmallIntegerField(
                        choices=[(0, "Basic"), (1, "Middle"), (2, "Advanced")],
                        default=0,
                    ),
                ),
                (
                    "image",
                    models.ImageField(default="default.png", upload_to="media/covers"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="quizzes",
                        to="quizez.category",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Result",
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
                ("create_datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="quizez.quiz",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Question",
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
                ("create_datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                (
                    "order_number",
                    models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(20)]),
                ),
                ("text", models.CharField(max_length=512)),
                (
                    "quiz",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="quizez.quiz",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Choice",
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
                ("create_datetime", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_update", models.DateTimeField(auto_now=True, null=True)),
                ("text", models.CharField(max_length=128)),
                ("is_correct", models.BooleanField(default=False)),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="choices",
                        to="quizez.question",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
