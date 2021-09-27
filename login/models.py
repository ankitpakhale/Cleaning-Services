from django.db import models

# Create your models here.

class login(models.Model):
    name = models.TextField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField(default='')
    def __str__(self):
        return self.name
        