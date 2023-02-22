from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name


class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel')
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.image.name


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
