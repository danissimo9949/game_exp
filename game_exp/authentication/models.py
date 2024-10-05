from django.db import models
from django.contrib.auth.models import User

class GameExpUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    is_player = models.BooleanField()
    is_developer = models.BooleanField()
    is_apply_news = models.BooleanField()
    is_accepting_terms = models.BooleanField()

    def __str__(self):
        return f'{self.user.username} | {self.user.email}'
    
    class Meta:
        verbose_name = 'GameExpUser'
        verbose_name_plural = 'GameExpUsers'
       
