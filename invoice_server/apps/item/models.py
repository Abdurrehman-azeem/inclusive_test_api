from django.db import models
from apps.invoice.models import Invoice

# Create your models here.
class Item(models.Model):
    invoice_id              = models.ForeignKey(Invoice, on_delete=models.PROTECT)
    item_name               = models.CharField(max_length = 150)
    amount                  = models.DecimalField(max_digits=9999, decimal_places=2)