# Generated by Django 4.2.6 on 2023-10-28 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rank_book_remove_history_book_to_book_books_count_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
    ]
