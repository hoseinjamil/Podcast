from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from mutagen.mp3 import MP3
from .validators import validate_mp3_file_extension
import os
from datetime import timedelta


class Podcast(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to='media', default='img_5.jpg', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    mp3_file = models.FileField(upload_to='podcasts/')
    duration = models.DurationField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.date} - {self.author}"

    def formatted_duration(self):
        total_seconds = self.duration.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"



@receiver(post_save, sender=Podcast)
def update_duration(sender, instance, created, **kwargs):
    if created and instance.mp3_file:  # Only calculate duration for new instances
        mp3_path = instance.mp3_file.path
        if os.path.exists(mp3_path):
            audio = MP3(mp3_path)
            duration_seconds = audio.info.length  # Duration in seconds
            duration = timedelta(seconds=duration_seconds)
            instance.duration = duration
            instance.save(update_fields=['duration'])