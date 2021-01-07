from django.db import models

# Create your models here.
class Categrory(models.Model):
    cname=models.CharField(max_length=30)

    def __str__(self):
        return self.cname
        
    class Meta:
        db_table='category'
    


class Product(models.Model):
    pname=models.CharField(max_length=30)
    pcat=models.ForeignKey(Categrory,on_delete=models.CASCADE)    
    price=models.DecimalField(decimal_places=2,max_digits=18)
    photo=models.ImageField(upload_to='products')

    def __str__(self):
        return self.pname

    class Meta:
        db_table='products'

class User(models.Model):
    userid=models.CharField(primary_key=True,max_length=30)
    uname=models.CharField(max_length=30)
    pwd=models.CharField(max_length=20)
    role=models.CharField(max_length=12)

    class Meta:
        db_table='users'


class Customer(models.Model):
    cname=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    gender=models.CharField(max_length=12)
    email=models.CharField(max_length=40)
    
    def __str__(self):
        return self.cname

    class Meta:
        db_table='customers'

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE) 
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    qty=models.IntegerField()

    def amount(self):
        return self.qty*self.product.price

    class Meta:
        db_table='cart'
