from django.db.models import Sum, F, Q

def filter_results(request, queryset):
    if 'date_gte' in request.query_params:
        date_gte = request.query_params['date_gte']
    else:
        date_gte = None
        
    if 'date_lte' in request.query_params:
        date_lte = request.query_params['date_lte']
    else:
        date_lte = None
        
    if 'order_date' in request.query_params:
        order = request.query_params['order_date']
    else:
        order = None        

    if date_gte != None and date_lte != None:
        queryset = queryset.filter(Q(date__lte=date_lte) & Q(date__gte=date_gte))
    elif date_gte != None and date_lte == None:
        queryset = queryset.filter(Q(date__gte=date_gte))
    elif date_lte != None and date_gte == None:
        queryset = queryset.filter(Q(date__lte=date_lte))
    else:
        queryset = queryset

    return queryset

def filter_total_price(request, Invoice):
        if 'order_price' in request.query_params:
            order_price = request.query_params['order_price']
        else:
            order_price = None

        if 'price_gte' in request.query_params:
            price_gte = request.query_params['price_gte']
        else:
            price_gte = None
        
        if 'price_lte' in request.query_params:
            price_lte = request.query_params['price_lte']
        else:
            price_lte = None

        if order_price != None or (price_lte != None or price_gte != None):
            price_lte = -1 if price_lte == None else price_lte
            price_gte = 0 if price_gte == None else price_gte
            order_price = 'asc' if order_price == None else order_price

            queryset = Invoice.objects.values('title', 'id', 'date')\
                .annotate(invoice_total_price = Sum('item__amount'))\
                .filter(Q(invoice_total_price__gte=price_gte) & Q(invoice_total_price__gte=price_lte))\
                .order_by(('-' if order_price == 'desc' else '') + 'invoice_total_price')
        else:
            queryset = Invoice.objects.values('title', 'id', 'date')\
            .annotate(invoice_total_price = Sum('item__amount'))  

        return queryset