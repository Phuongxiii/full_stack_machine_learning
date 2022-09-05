from rest_framework import serializers
from .models.image_dto import ImageDto


class ImageDtoSerializers(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.ImageField()
    create_at = serializers.DateTimeField()
    label = serializers.CharField()

    class Meta:
        model = ImageDto
        fields = ["title", "image", "create_at", "label"]
