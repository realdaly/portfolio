from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=1000, default="Empty")
    title = models.CharField(max_length=1000, default="Empty")
    paragraph = models.TextField(max_length=5000, default="Empty")
    profileImg = models.CharField(max_length=5000, default="Empty")
    coverImg = models.CharField(max_length=5000, default="Empty")

    def __str__(self):
        return f"{self.name}, {self.title}"


class Education(models.Model):
    year = models.IntegerField()
    description = models.TextField(max_length=5000, default="Empty")

    def __str__(self):
        return f"{self.year}"


class Skill(models.Model):
    name = models.CharField(max_length=1000, default="Empty")

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    name = models.CharField(max_length=1000, default="Empty")
    image = models.CharField(max_length=5000, default="Empty")
    link = models.CharField(max_length=5000, default="Empty")

    def __str__(self):
        return f"{self.name}"


class Hobby(models.Model):
    name = models.CharField(max_length=1000, default="Empty")

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=1000, default="Empty")
    content = models.CharField(max_length=5000, default="Empty")
    link = models.CharField(max_length=5000, default="Empty")

    def __str__(self):
        return f"{self.name}: {self.link}"