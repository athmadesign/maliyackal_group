from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    image = models.ImageField(upload_to='projects/')
    
    def __str__(self):
        return self.title