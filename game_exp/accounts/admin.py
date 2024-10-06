from django.contrib import admin
from .models import Language, Profile, GameExpUser

admin.site.register(Language)
admin.site.register(GameExpUser)
admin.site.register(Profile)