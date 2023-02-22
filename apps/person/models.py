from django.db import models
from main.models import Category


class About(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about')
    birthday = models.DateField()
    bio = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    projects = models.IntegerField(default=0)
    awards = models.IntegerField(default=0)
    customers = models.IntegerField(default=0)
    cups_of_coffee = models.IntegerField(default=0)
    cv = models.FileField(upload_to='about_cv')

    def __str__(self):
        return self.name


class Resume(models.Model):
    start = models.DateField()
    finish = models.DateField(null=True)
    profession = models.CharField(max_length=250)
    where = models.CharField(max_length=350)
    description = models.TextField()

    def __str__(self):
        return self.profession


class Service(models.Model):
    icon = models.CharField(max_length=250)
    profession = models.CharField(max_length=250)

    def __str__(self):
        return self.profession


class Skill(models.Model):
    profession = models.CharField(max_length=250)
    percent = models.IntegerField()

    def __str__(self):
        return self.profession


class Project(models.Model):
    image = models.ImageField(upload_to='projects')
    category = models.ManyToManyField(Category, blank=True)
    link = models.URLField(null=True, blank=True)
    profession = models.CharField(max_length=250)

    def __str__(self):
        return self.profession
