from django.db import models

# Create your models here.
class About(models.Model):
    greet = models.CharField(max_length=1000)
    info = models.CharField(max_length=5000)
    paragraph = models.TextField(max_length=1000)
    image = models.CharField(max_length=5000)

    def __str__(self):
        return f"{self.greet}"


class Education(models.Model):
    year = models.IntegerField()
    description = models.TextField(max_length=5000)

    def __str__(self):
        return f"{self.year}"


class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Project(models.Model):
    image = models.CharField(max_length=5000)
    link = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Hobby(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}: {self.link}"