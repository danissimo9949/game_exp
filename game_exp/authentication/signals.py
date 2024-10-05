from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import GameExpUser

@receiver(post_save, sender=GameExpUser)
def game_exp_created(sender, **kwargs):
    pass