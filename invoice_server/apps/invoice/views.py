from rest_framework import status, viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Invoice
from .serializer import InvoiceSerializer
from rest_framework.decorators import api_view
from .scripts.pdf_generator import generate_pdf
from django.shortcuts import HttpResponse
from django.db.models import Sum, F
from .filter import filter_results, filter_total_price

# Create your views here.
class InvoiceViewset(viewsets.ViewSet):
    parser_classes      = (FormParser, MultiPartParser)
    queryset            = Invoice.objects.all()

    #lists all the items associated to an invoice
    def list(self, request):
        queryset = filter_total_price(request, Invoice)
        invoices = filter_results(request, queryset)
        #print(invoices)
        serializer  = InvoiceSerializer(invoices, many = True)
        print(serializer.data)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def create(self, request):
        serializer  = InvoiceSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        queryset    = self.queryset
        invoice     = get_object_or_404(queryset, pk = pk)
        serializer  = InvoiceSerializer(invoice)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def partial_update(self, request, pk = None):
        queryset    = self.queryset
        invoice     = get_object_or_404(queryset, pk = pk)
        serializer  = InvoiceSerializer(invoice, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)

    def destroy(self, request, pk = None):
        queryset    = self.queryset
        invoice     = get_object_or_404(queryset, pk = pk)
        invoice.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def download_invoice(request, pk = None):
    queryset    = Invoice.objects.all()
    invoice     = get_object_or_404(queryset, pk=pk)
    template    = 'invoice/invoice.html'
    
    items       = []
    for _ in invoice.item_set.all():
        items.append([_.item_name, _.amount])
    
    context_dict    = {
        'title': invoice.title,
        'date' : invoice.date,
        'image' : invoice.reciept_image,
        'items' : items
    }

    pdf = generate_pdf(template, context_dict, request)

    if pdf == None:
        Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = 'invoice.pdf'
    content  = 'inline; attachment; filename="%s"' %(filename)
    response['Content-Disposition'] = content
    return response