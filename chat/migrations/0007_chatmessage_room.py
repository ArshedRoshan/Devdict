# Generated by Django 4.0.6 on 2023-01-07 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_remove_chatmessage_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='room',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='chat.chatroom'),
        ),
    ]
