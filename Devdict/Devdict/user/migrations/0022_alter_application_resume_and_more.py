# Generated by Django 4.0.6 on 2023-03-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_user_is_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='resume',
            field=models.FileField(upload_to='static/', verbose_name='resume'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
    ]
