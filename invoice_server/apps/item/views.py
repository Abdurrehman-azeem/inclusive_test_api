from django.shortcuts import get_object_or_404
from .serializer import ItemSerializer
from .models import Item
from rest_framework import status, viewsets, renderers
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.decorators import action

# Create your views here.

class ItemViewset(viewsets.ViewSet):
    
    def list(self, request):
        # exception statement needed incase no foreignkey provided
        items           = Item.objects.all().filter(invoice_id = request.data['invoice_id'])
        serializer      = ItemSerializer(items, many = True)
        return Response(serializer.data)

    def create(self, request):
        serializer      = ItemSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = status.HTTP_201_CREATED)
        return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)     

    def destroy(self, request, pk = None):
        queryset        = Item.objects.all()
        item            = get_object_or_404(queryset, pk = pk)
        item.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk = None):
        queryset        = Item.objects.all()
        item            = get_object_or_404(queryset, pk = pk)
        serializer      = ItemSerializer(item, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status = status.HTTP_304_NOT_MODIFIED)

    def retrieve(self, request, pk = None):
        queryset        = Item.objects.all()
        item            = get_object_or_404(queryset, pk = pk)
        serializer      = ItemSerializer(item)
        return Response(serializer.data, status = status.HTTP_200_OK)