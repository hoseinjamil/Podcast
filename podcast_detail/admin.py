from django.contrib import admin
from . import models

class PodcastAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    fields = ('title', 'body', 'image', 'mp3_file', 'duration', 'author', 'date')

admin.site.register(models.Podcast, PodcastAdmin)