from django import forms
from .models import Podcast



class AddPodcastForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = ['title', 'body', 'image', 'mp3_file', 'duration', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'mp3_file': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'duration': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }