from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ImageDto
import base64

# Create your views here.


@api_view(["GET", "POST"])
def word_recognition(request, pk):
    try:
        imageDto = ImageDto.objects.get(pk=pk)
    except ImageDto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    image_base64 = base64.b64encode(imageDto.image)
    return Response({
        imageDto.title, image_base64, imageDto.create_at
    })
