from django.contrib import admin

# Register your models here.

from .models.image_dto import ImageDto

admin.site.register(ImageDto)
