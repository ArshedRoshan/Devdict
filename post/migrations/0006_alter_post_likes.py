# Generated by Django 4.0.6 on 2022-12-08 06:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_alter_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(default=True, related_name='posts_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
