# Generated by Django 4.0.6 on 2022-12-13 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_follower_follow_followed_by_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='follow',
        ),
    ]
