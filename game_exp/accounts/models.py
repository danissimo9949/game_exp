from typing import Iterable
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

class Token(models.Model):
    refresh_token = models.CharField(max_length=500, blank=True, null=True)
    expired_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Refresh token: {self.refresh_token}. Expired at: {self.expired_at}"
    
class GameExpUser(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    token = models.OneToOneField(Token, on_delete=models.CASCADE, blank=True, null=True)
    is_player = models.BooleanField()
    is_developer = models.BooleanField()
    is_apply_news = models.BooleanField()
    is_accepting_terms = models.BooleanField()
    is_two_auth_enabled = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} | {self.user.email}'
    
    class Meta:
        verbose_name = 'GameExpUser'
        verbose_name_plural = 'GameExpUsers'



class Language(models.Model):
    lang_name = models.CharField()
    choose_rate = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.lang_name}"
    
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Profile(models.Model):
    user = models.OneToOneField(GameExpUser, on_delete=models.CASCADE)
    profile_name = models.CharField(max_length=100, blank=True, null=True)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile-images/', blank=True, null=True)
    profile_url = models.URLField(blank=True, null=True)
    twitter_link = models.CharField(blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    profile_content = models.TextField(blank=True, null=True)
    additional_email = models.EmailField(blank=True, null=True)
    
    def set_profile_name(self):
        if self.user and not self.profile_name:
            self.profile_name = self.user.user.username

    def set_display_name(self):
        if self.user and not self.display_name:
            self.display_name = self.user.user.username

    def generate_profile_link(self):
        if(self.user):
            self.profile_url = f"http://127.0.0.1/users/profile/{self.user.user.username}"

    def __str__(self):
        return f'Profile {self.profile_name} owned by user {self.user.user.username}'
    
   
    def save(self, *args, **kwargs):
        self.set_profile_name()
        self.generate_profile_link()
        self.set_display_name()
        return super().save()
    
    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'


class EmailNotification(models.Model):
    user = models.OneToOneField(GameExpUser, on_delete=models.CASCADE)
    is_never_send = models.BooleanField(default=False)

    buy_notification = models.BooleanField(default=True)
    follow_notification = models.BooleanField(default=True)
    reply_notification = models.BooleanField(default=True)
    sales_notification = models.BooleanField(default=True)

    new_features_announced = models.BooleanField(default=True)
    new_game_jams = models.BooleanField(default=True)
    new_devblogs_following = models.BooleanField(default=True)
    new_uploads_add = models.BooleanField(default=True)

    def __str__(self):
        return f"Email notifications for {self.user.user.username} account"
    
    class Meta:
        verbose_name = "Email notification"
        verbose_name_plural = "Email notifications"

    