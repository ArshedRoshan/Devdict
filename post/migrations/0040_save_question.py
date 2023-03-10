# Generated by Django 4.0.6 on 2023-01-11 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0039_comment_reply'),
    ]

    operations = [
        migrations.CreateModel(
            name='save_question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_question', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='post.question')),
                ('user', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
