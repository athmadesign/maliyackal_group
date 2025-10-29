from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='services/thumbnails/', blank=True, null=True)
    image = models.ImageField(upload_to='services/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title