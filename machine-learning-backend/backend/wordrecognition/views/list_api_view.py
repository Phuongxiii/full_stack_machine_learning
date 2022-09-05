from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from wordrecognition.serializers import ImageDtoSerializers
from wordrecognition.models.image_dto import ImageDto


class ListAPIView(generics.ListAPIView):
    queryset = ImageDto.objects.all()
    serializer_class = ImageDtoSerializers
    # lookup_field = "pk"


listAPIView = ListAPIView.as_view()
