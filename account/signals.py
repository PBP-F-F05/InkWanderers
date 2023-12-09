from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile, Rank_Book, History_Book
from collection.models import Collection
from bookmarks.models import BookmarkList

@receiver(post_save, sender=User)
def create_user_needs_class(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
        rank_book = Rank_Book(profile = user_profile)
        rank_book.save()
        hisotry_book = History_Book(profile = user_profile)
        hisotry_book.save()
        owner = Profile.objects.filter(user = instance)[0]
        collection = Collection(owner= owner)
        collection.save()
        bookmark_list = BookmarkList(user=owner)
        bookmark_list.save()
