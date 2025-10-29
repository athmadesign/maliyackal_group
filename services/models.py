from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    description = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='services/thumbnails/', blank=True, null=True)
    image = models.ImageField(upload_to='services/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title