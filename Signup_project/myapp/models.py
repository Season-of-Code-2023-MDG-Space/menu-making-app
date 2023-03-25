from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Normal(models.Model):
    fullname = models.CharField(max_length=200, blank=True, null=True, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.fullname

class Gravy(models.Model):
    gravy = models.CharField(max_length=200, blank=True, null=True, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.gravy

class Snacks(models.Model):
    snacks = models.CharField(max_length=200, blank=True, null=True, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.snacks

class Sweets(models.Model):
    sweets = models.CharField(max_length=200, blank=True, null=True, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.sweets


class Breakfast(models.Model):
    breakfast = models.CharField(max_length=200)


class MyTable(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()


class MenuName(models.Model):
    name_of_chart = models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_chart
    
class Charts(models.Model):
    
    menuname = models.ForeignKey(MenuName, on_delete=models.CASCADE, null=True)
    DAY_CHOICES = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )
    MEAL_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    )
    
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    meal = models.CharField(max_length=9, choices=MEAL_CHOICES)
    item = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.day} - {self.meal}: {self.item}"
    

class MenuItem(models.Model):
    
    DAY_CHOICES = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )
    MEAL_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    )
    
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    meal = models.CharField(max_length=9, choices=MEAL_CHOICES)
    item = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.day} - {self.meal}: {self.item}"

class Post(models.Model):
    DAY_CHOICES = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )
    MEAL_CHOICES = (
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    )
    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    meal = models.CharField(max_length=9, choices=MEAL_CHOICES)
    item = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.day} - {self.meal}: {self.item}"

    
