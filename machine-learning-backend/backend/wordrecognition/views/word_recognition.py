from django.shortcuts import get_object_or_404
from rest_framework import generics, mixins, Response
from wordrecognition.serializers import ImageDtoSerializers
from wordrecognition.models.image_dto import ImageDto
from wordrecognition.controllers.model_tensorflow import ModelTensorflow
# Create your views here.


class ApiView(generics.GenericAPIView, mixins.ListModelMixin):
    # lookup_field = 'pk'
    queryset = ImageDto.objects.all()
    serializer_class = ImageDtoSerializers
    model = ModelTensorflow()

    def post(self,request, *args, **kwargs):
        return Response(request.data)


word_recognition = ApiView.as_view()
