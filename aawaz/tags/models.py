from unicodedata import name
from django.db import models
from user_management.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.

class Tags(BaseModel):
    tag_name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    def __str__(self):
        return self.tag_name

class Category(BaseModel):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Label(BaseModel):
    label_name = models.CharField(max_length=35)
    users = models.ManyToManyField(User)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.label_name

