from rest_framework import serializers
from .models import ImageDto


class ImageDtoSerializers(serializers.Serializer):
    title = serializers.TextField()
    image = serializers.Imagefield()
    create_at = serializers.DateTimeField(auto_now_add=True)
    label = serializers.CharField()

    class Meta:
        model = ImageDto
        fields = ["title", "image", "label"]

    def create(self, validated_data):
        return ImageDto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.label = validated_data.get('label', instance.label)
        return instance
