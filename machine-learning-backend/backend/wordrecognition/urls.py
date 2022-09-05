
from django.urls import path
from wordrecognition.views.list_api_view import listAPIView
from wordrecognition.views.word_recognition import word_recognition


urlpatterns = [
    path('<int:pk>', view=word_recognition, name="word_recognition"),
    path('', view=listAPIView, name="word_recognition"),
]
