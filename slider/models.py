from django.db import models

# Create your models here.


class Slide(models.Model):
    image = models.ImageField(upload_to="slide")
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
