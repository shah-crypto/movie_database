# Generated by Django 3.1.7 on 2021-07-23 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_movie_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
