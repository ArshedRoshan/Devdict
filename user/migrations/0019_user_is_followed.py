# Generated by Django 4.0.6 on 2023-01-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0018_user_is_verfied'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_followed',
            field=models.BooleanField(default=False),
        ),
    ]
