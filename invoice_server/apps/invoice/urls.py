from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewset, download_invoice
from apps.item.views import ItemViewset
from django.conf.urls.static import static
from invoice_server import settings

router = DefaultRouter()
router.register('', InvoiceViewset, basename='invoice')

urlpatterns = [
    path('invoices/', include(router.urls)),
    path('invoice/item/', include('apps.item.urls')),
    path('invoice/<int:pk>/download/', download_invoice)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

