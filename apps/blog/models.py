from django.db import models
from person.models import About
from main.models import Category


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=350)
    image = models.ImageField(upload_to='blogs')
    category = models.ForeignKey(Category, models.CASCADE)
    tags = models.ManyToManyField(Tag)
    content = models.TextField()
    author = models.ForeignKey(About, models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, models.CASCADE)
    name = models.CharField(max_length=350)
    email = models.EmailField()
    image = models.ImageField(upload_to='comment', null=True)
    website = models.URLField(null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
