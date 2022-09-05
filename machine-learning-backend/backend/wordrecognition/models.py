from django.db import models
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import cv2 as cv
from tensorflow.keras.layers.experimental.preprocessing import StringLookup


class ModelTensorflow():
    np.random.seed(42)
    tf.random.set_seed(42)
    path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "wordrecognition\\data\\saved_model\\my_model")
    characters_1 = []
    max_len = 21

    def __init__(self):
        path_character = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "wordrecognition\\data\\chars.txt")
        self.characters = open(path_character, "r").readlines()
        for i in self.characters:
            a = i[0]
            self.characters_1.append(a)
        AUTOTUNE = tf.data.AUTOTUNE

        # Mapping characters to integers.
        self.char_to_num = StringLookup(
            vocabulary=list(self.characters_1), mask_token=None)

        # Mapping integers back to original characters.
        self.num_to_char = StringLookup(
            vocabulary=self.char_to_num.get_vocabulary(), mask_token=None, invert=True
        )

    def decode_batch_predictions(self, pred):
        input_len = np.ones(pred.shape[0]) * pred.shape[1]
        # Use greedy search. For complex tasks, you can use beam search.
        results = tf.keras.backend.ctc_decode(pred, input_length=input_len, greedy=True)[0][0][
            :, :self.max_len
        ]
        # Iterate over the results and get back the text.
        output_text = []
        for res in results:
            res = tf.gather(res, tf.where(tf.math.not_equal(res, -1)))
            res = tf.strings.reduce_join(
                self.num_to_char(res)).numpy().decode("utf-8")
            output_text.append(res)
        return output_text

    def load_model(self):
        self.model = tf.keras.models.load_model(self.path)
        return tf.keras.models.Model(
            self.model.get_layer(name="image").input, self.model.get_layer(
                name="dense2").output
        )

    def get_result(self, result):
        r = self.decode_batch_predictions(result)
        return r[0]

    def getModel(self):
        return self.model

    def getPath(self):
        return self.path

    def distortion_free_resize(self, image, img_size):
        w, h = img_size
        image = tf.image.resize(image, size=(h, w), preserve_aspect_ratio=True)

        # Check tha amount of padding needed to be done.
        pad_height = h - tf.shape(image)[0]
        pad_width = w - tf.shape(image)[1]

        # Only necessary if you want to do same amount of padding on both sides.
        if pad_height % 2 != 0:
            height = pad_height // 2
            pad_height_top = height + 1
            pad_height_bottom = height
        else:
            pad_height_top = pad_height_bottom = pad_height // 2

        if pad_width % 2 != 0:
            width = pad_width // 2
            pad_width_left = width + 1
            pad_width_right = width
        else:
            pad_width_left = pad_width_right = pad_width // 2

        image = tf.pad(
            image,
            paddings=[
                [pad_height_top, pad_height_bottom],
                [pad_width_left, pad_width_right],
                [0, 0],
            ],
        )

        image = tf.transpose(image, perm=[1, 0, 2])
        image = tf.image.flip_left_right(image)
        return image


# Create your models here.

class ImageDto(models.Model):
    title = models.TextField(max_length=50, default="image")
    image = models.ImageField()
    create_at = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=21)


class WordRecognition(models.Model):
    image = models.ForeignKey(ImageDto, on_delete=models.CASCADE)
    modelTf = ModelTensorflow()

    def __init__(self):
        self.model = self.modelTf.load_model()

    def recognition(self, image):
        result = self.model.predict(image)
        return self.modelTf.get_result(result=result)

    def update_label(self, image):
        return ImageDto.objects.create(**image)
