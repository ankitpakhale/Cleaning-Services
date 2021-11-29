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
    quantity=models.PositiveIntegerField(default=1)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True,null=True)
    update_on= models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.person.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    oemail=models.EmailField(default='')
    name=models.CharField(max_length=25,default='')
    services=models.CharField(max_length=500,default='')
    adddress=models.CharField(max_length=200,default='')
    contact=models.CharField(max_length=11,default='')
    service_date=models.DateField(auto_now_add=True)
    amount=models.PositiveIntegerField(default=None)

    def __str__(self) -> str:
        return self.services

class DonateMoney(models.Model):
    person = models.ForeignKey(signUp,on_delete=models.CASCADE, null=True)
    amount=models.PositiveIntegerField(null=True)
    added_on= models.DateTimeField(auto_now_add=True, null=True)
    
    def __unicode__(self):
        return self.person

