from django.db import models


class ImageDto(models.Model):
    title = models.TextField(max_length=50, default="image")
    image = models.ImageField(upload_to='static/')
    create_at = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=21, default="")
