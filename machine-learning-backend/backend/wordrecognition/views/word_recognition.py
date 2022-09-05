
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from wordrecognition.serializers import ImageDtoSerializers
from wordrecognition.models.image_dto import ImageDto
from wordrecognition.controllers.model_tensorflow import ModelTensorflow

# Create your views here.


@api_view(["GET", "POST"])
def word_recognition(request, pk):
    try:
        imageDto = ImageDto.objects.get(pk=pk)
    except ImageDto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    model_tf = ModelTensorflow()
    result = model_tf.recognition(image=imageDto.image)
    return Response({
        imageDto.title, imageDto.create_at, imageDto.label, result
    })
