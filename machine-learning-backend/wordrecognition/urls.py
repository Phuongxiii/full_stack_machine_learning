
from django.urls import path
from wordrecognition.views.list_api_view import listAPIView
from wordrecognition.views.word_recognition import word_recognition


urlpatterns = [
    path('predict/', view=word_recognition, name="word_recognition_predict"),
    path('', view=listAPIView, name="word_recognition"),
]
