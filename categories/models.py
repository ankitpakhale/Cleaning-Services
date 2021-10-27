from django.db import models
from signup.models import signUp

class item(models.Model):
    images = models.ImageField(upload_to='pro_img',blank=True)
    title = models.CharField(default='', max_length=20)
    price = models.PositiveIntegerField(default='')
    description = models.CharField(default='', max_length=90)
    def __str__(self):
        return self.title

class MyCart(models.Model):
    person = models.ForeignKey(signUp,on_delete=models.CASCADE)
    book = models.ForeignKey(item,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    update_on= models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.person.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(signUp,on_delete=models.CASCADE)
    items = models.CharField(max_length=100)
    order_amount = models.CharField(max_length=80)
    ordered_on = models.DateTimeField(auto_now_add=True,null=True)
    qrimage = models.ImageField(upload_to='qrimage',blank=True,null=True)
    invoice = models.FileField(default='')

    def __str__(self):
        return self.items