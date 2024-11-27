from django.db import models

# makemigration - create change and store it in a file
# migration - apply the pending changes created by makemigration

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.email
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    img_url = models.CharField(max_length=200)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True) 