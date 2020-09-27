from django.db.models import Q

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

    if 'order_price' in request.query_params:
        order_price = request.query_params['order_price']
    else:
        order_price = None 

        

    if date_gte != None and date_lte != None:
        queryset = queryset.filter(Q(date__lte=date_lte) & Q(date__gte=date_gte))
    elif date_gte != None and date_lte == None:
        queryset = queryset.filter(Q(date__gte=date_gte))
    elif date_lte != None and date_gte == None:
        queryset = queryset.filter(Q(date__lte=date_lte))
    else:
        queryset = queryset
        

    if order != None:
        if order == 'desc':
            queryset = queryset.filter().order_by('-date')
        else:
            queryset = queryset.filter().order_by('date')
    else:
        pass 

    if order_price != None:
        if order_price == 'desc':
            queryset = queryset.filter().order_by('-total_price')
        else:
            queryset = queryset.filter().order_by('total_price')
    else:
        pass

    return queryset