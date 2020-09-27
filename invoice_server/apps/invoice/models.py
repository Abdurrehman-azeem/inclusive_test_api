from django.db import models
from datetime import datetime

# Create your models here.
class Invoice(models.Model):
    title                   = models.CharField(max_length = 150)
    reciept_image           = models.ImageField(upload_to='invoice_receipts/%Y/%m/%d', null = True, blank = True)
    date                    = models.DateTimeField(default=datetime.now)


# class Item(models.Model):
#     invoice_id              = models.ForeignKey(Invoice, on_delete=models.PROTECT)
#     item_name               = models.CharField(max_length = 150)
#     amount                  = models.DecimalField(max_digits=9999, decimal_places=2)
