# Generated by Django 4.0.6 on 2023-01-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_rename_is_followed_user_is_follow_user_is_follower'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_block',
            field=models.BooleanField(default=True),
        ),
    ]
