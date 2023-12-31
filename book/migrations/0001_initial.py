# Generated by Django 4.2.6 on 2023-10-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('categories', models.CharField(max_length=255)),
                ('thumbnail', models.TextField()),
                ('description', models.TextField()),
                ('published_year', models.IntegerField()),
                ('is_borrowed', models.BooleanField(default=False)),
                ('review_count', models.IntegerField(default=0)),
                ('review_points', models.IntegerField(default=0)),
            ],
        ),
    ]
