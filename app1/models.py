from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25, default='')
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CategoryName = models.ForeignKey(Category, on_delete=models.CASCADE)
    ownerName = models.CharField(max_length=255)
    descriptionOfCategory = models.TextField()
    priceOfProduct = models.IntegerField(default='')
    registration_date = models.DateField()
    rating = models.IntegerField(default='')
    def __str__(self):
        return self.ownerName

class xyz(models.Model):
    name = models.TextField(max_length=30, default='')
    email = models.EmailField(default='')
    number = models.PositiveIntegerField(default='')
    def __str__(self):
        return self.name

class item(models.Model):
    title = models.CharField(default='', max_length=20)
    price = models.PositiveIntegerField(default='')
    description = models.CharField(default='', max_length=90)
    def __str__(self):
        return self.title
