# from django.db import models
# from wordrecognition.controllers.model_tensorflow import ModelTensorflow
# from wordrecognition.models.image_dto import ImageDto


# class WordRecognition(models.Model):
#     image = models.ForeignKey(ImageDto, on_delete=models.CASCADE)
#     modelTf = ModelTensorflow()

#     def __init__(self):
#         self.model = self.modelTf.load_model()

#     def recognition(self, image):
#         result = self.model.predict(image)
#         return self.modelTf.get_result(result=result)

#     def update_label(self, image):
#         return ImageDto.objects.create(**image)
