
# Generated by Django 4.2.6 on 2023-10-28 09:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_book_to_book',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
