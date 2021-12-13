# A signal is a receiver - When an object (in this case User object) is created a signal will be fired
# to this signals.py. The receiver picks up that signal and then the respective function is called (in thi
# case create_profiles)

# We need to wire this signals.py file in to the apps.py by overriding the ready method

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import UserProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: # If the User object is created then we create a UserProfile
        userprofile = UserProfile.objects.create(user=instance)