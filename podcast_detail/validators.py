from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_mp3_file_extension(value):
    if not value.name.endswith('.mp3'):
        raise ValidationError(_('Only MP3 files are allowed.'))