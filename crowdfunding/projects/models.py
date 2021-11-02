from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.URLField(
        default="https://i.pinimg.com/originals/8f/05/17/8f0517135e33a3f1ad573d1dc16318b9.jpg"
    )
    is_active = models.BooleanField(default=True)
    goal = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    close_date = models.DateTimeField(null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=400, null=True)
    anonymous = models.BooleanField(default=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)


class Perk(models.Model):
    name = models.CharField(max_length=150)
    minValue = models.IntegerField(default=0)
    qtyLimit = models.IntegerField(null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
