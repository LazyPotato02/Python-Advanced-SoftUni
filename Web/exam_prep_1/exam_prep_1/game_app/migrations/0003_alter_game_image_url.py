# Generated by Django 4.1.2 on 2022-10-29 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_app', '0002_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image_url',
            field=models.URLField(),
        ),
    ]
