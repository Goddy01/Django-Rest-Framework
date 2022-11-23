from django.db import models
from django.conf import settings

# Create your models here.
# User = settings.AUTH_USER_MODEL
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content= models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, default=99.99, decimal_places=2)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price)*0.8)

    def get_discount(self):
        return '122'