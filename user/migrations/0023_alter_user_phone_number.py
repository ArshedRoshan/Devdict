# Generated by Django 4.0.6 on 2023-03-07 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_alter_application_resume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
