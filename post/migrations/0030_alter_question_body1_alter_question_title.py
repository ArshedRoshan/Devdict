# Generated by Django 4.0.6 on 2022-12-15 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0029_rename_body_question_body1_question_body2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
