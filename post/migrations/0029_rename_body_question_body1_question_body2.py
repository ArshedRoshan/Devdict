# Generated by Django 4.0.6 on 2022-12-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0028_question_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='body',
            new_name='body1',
        ),
        migrations.AddField(
            model_name='question',
            name='body2',
            field=models.CharField(default=True, max_length=500),
        ),
    ]
