# Generated by Django 4.1 on 2022-08-20 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordrecognition', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageDto',
        ),
        migrations.DeleteModel(
            name='WordRecognition',
        ),
    ]
