# Generated by Django 4.1 on 2022-09-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordrecognition', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedto',
            name='label',
            field=models.CharField(default='', max_length=21),
        ),
    ]