# Generated by Django 4.0.6 on 2022-12-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
