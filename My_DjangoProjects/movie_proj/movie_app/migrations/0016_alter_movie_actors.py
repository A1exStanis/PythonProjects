# Generated by Django 5.0.2 on 2024-04-17 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0015_remove_director_slug_alter_movie_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='movie_app.actor'),
        ),
    ]
