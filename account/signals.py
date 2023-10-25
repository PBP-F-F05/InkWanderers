from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile, History_Book

@receiver(post_save, sender=User)
def create_keranjang_belanja(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
        history_book = History_Book(profile = user_profile)
        history_book.save()
