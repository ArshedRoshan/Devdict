# Generated by Django 4.0.6 on 2022-12-08 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
