from django.db import models

# Create your models here.

class Normal(models.Model):
    fullname = models.CharField(max_length=200)

    def __str__(self):
        return self.fullname

class Gravy(models.Model):
    gravy = models.CharField(max_length=200)

    def __str__(self):
        return self.gravy

class Snacks(models.Model):
    snacks = models.CharField(max_length=200)

    def __str__(self):
        return self.snacks

class Sweets(models.Model):
    sweets = models.CharField(max_length=200)

    def __str__(self):
        return self.sweets
