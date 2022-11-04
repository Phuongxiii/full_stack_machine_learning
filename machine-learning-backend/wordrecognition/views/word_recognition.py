import base64
import numpy as np
from PIL import Image
import tensorflow as tf
from io import BytesIO
from rest_framework import generics, mixins
from rest_framework.response import Response
from wordrecognition.serializers import ImageDtoSerializers
from wordrecognition.models.image_dto import ImageDto
from wordrecognition.controllers.model_tensorflow import ModelTensorflow

class ApiView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = ImageDto.objects.all()
    serializer_class = ImageDtoSerializers
    model = ModelTensorflow()

    def post(self,request, *args, **kwargs):
        data = request.data['image'][22:]
        image = Image.open(BytesIO(base64.b64decode(data)))
        result = self.model.recognition(image)
        return Response({"image": result})


word_recognition = ApiView.as_view()
