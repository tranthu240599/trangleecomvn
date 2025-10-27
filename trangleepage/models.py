from django.db import models
from django.utils import timezone


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(default=timezone.now)
