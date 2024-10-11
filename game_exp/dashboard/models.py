from django.db import models
from django.shortcuts import get_object_or_404
from accounts.models import GameExpUser, Profile
from taggit.managers import TaggableManager

class ProjectClassification(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return f'Project classification: {self.name}'

    class Meta:
        verbose_name = 'Classification'
        verbose_name_plural = 'Classifications'

class ProjectGenre(models.Model):
    genre = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f'Project genre: {self.genre}'

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Project(models.Model):
    creator = models.ForeignKey(GameExpUser, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=150, blank=False, null=False)
    project_url = models.URLField(max_length=255, blank=False, null=False)
    project_short_desc = models.CharField(max_length=150, blank=True, null=True)
    project_classification = models.ForeignKey(ProjectClassification, on_delete=models.SET_NULL, blank=True, null=True)
    project_details = models.TextField(blank=False, null=False)
    project_genre = models.ForeignKey(ProjectGenre, on_delete=models.SET_NULL, blank=True, null=True)
    project_tags = TaggableManager()
    
    # Additional links
    steam_url = models.URLField(blank=True, null=True)
    googleplay_url = models.URLField(blank=True, null=True)

    # Pricing variant
    free_or_donate = models.BooleanField(default=True, blank=True, null=True)
    is_paid = models.BooleanField(default=False, blank=True, null=True)
    is_free = models.BooleanField(default=False, blank=True, null=True)
    suggested_donation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Community fields
    disabled_community = models.BooleanField(default=False, blank=True, null=True)
    comments_allow = models.BooleanField(default=True, blank=True, null=True)
    dedicated_community_page = models.BooleanField(default=False, blank=True, null=True)

    # Visibility settings
    is_draft = models.BooleanField(default=True, blank=True, null=True)
    is_restricted = models.BooleanField(default=False, blank=True, null=True)
    is_public = models.BooleanField(default=False, blank=True, null=True)

    # Stats
    dowloads_count = models.IntegerField(default=0)
    project_views = models.IntegerField(default=0)

    # More information about project
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def set_project_url(self):
        if self.project_title:
            self.project_url = f'http://127.0.0.1/dashboard/project/{self.project_title}'

    def increment_downloads(self):
        self.dowloads_count += 1
        self.save(update_fields=['downloads_count'])

    def increment_views(self):
        self.project_views += 1
        self.save(update_fields=['project_views'])

    def __str__(self):
        profile = get_object_or_404(Profile, user=self.creator.user)
        return f'Project: {self.project_title} from user - {profile.profile_name}'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'