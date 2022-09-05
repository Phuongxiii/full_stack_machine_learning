
from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>', view=views.word_recognition, name="word_recognition"),
]
