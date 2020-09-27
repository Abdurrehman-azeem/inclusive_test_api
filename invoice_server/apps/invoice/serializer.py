from rest_framework import serializers
from .models import Invoice
from apps.item.serializer import ItemSerializer

# class ItemSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Item
#         fields = ['id', 'invoice_id', 'item_name', 'amount']

class InvoiceSerializer(serializers.ModelSerializer):
    
    item_set = ItemSerializer(many = True, read_only = True)

    class Meta:
        model = Invoice
        fields = ['id', 'title', 'reciept_image', 'date', 'item_set']
