# Generated by Django 3.1.7 on 2021-06-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('genre', models.CharField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('comedy', 'Comedy'), ('crime_mystery', 'Crime & Mystery'), ('fantasy', 'Fantasy'), ('historical', 'Historical'), ('horror', 'Horror'), ('romance', 'Romance'), ('sci_fi', 'Science fiction'), ('thriller', 'Thriller'), ('western', 'Western')], max_length=15, null=True)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('preview_image', models.ImageField(null=True, upload_to='photos/')),
                ('movie_image', models.ImageField(upload_to='photos/')),
                ('year_of_release', models.PositiveIntegerField()),
                ('movie_time', models.TimeField()),
                ('director', models.CharField(max_length=100)),
                ('cast', models.TextField()),
                ('link', models.TextField(null=True)),
            ],
        ),
    ]
