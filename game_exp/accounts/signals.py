from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import GameExpUser, Profile, Language, EmailNotification

@receiver(post_save, sender=GameExpUser)
def game_exp_created(sender, instance, created, **kwargs):
    if created:
        default_language = Language.objects.get(lang_name='English')

        profile = Profile.objects.create(user=instance, language=default_language)
        profile.save()

        notification_settings = EmailNotification.objects.create(user=instance)
        notification_settings.save()
        