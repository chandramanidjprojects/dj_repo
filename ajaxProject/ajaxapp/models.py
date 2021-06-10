from django.db import models
from django.urls import reverse
class Student(models.Model):
  name=models.CharField(max_length=32)
  marks=models.IntegerField()
  def __str__(self):
    return self.name
  