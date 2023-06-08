"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    """Post model."""

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    position = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{}'.format(self.title)
