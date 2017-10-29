from django.shortcuts import render
import services
from bson.objectid import ObjectId
from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework import permissions, status, parsers, renderers, generics
from rest_framework.response import Response
from analytic.models import Customer,Order
from analytic.serializers import CustomerSerializer,OrderSerializer
from rest_framework.exceptions import NotFound


def error404(request):
    raise NotFound(detail="Error 404, page not found", code=404)

class CustomersViewSet(ModelViewSet):

    serializer_class = CustomerSerializer
    lookup_field = 'customerId'
    lookup_url_kwarg = 'customerId'

    def get_queryset(self):
        services.getAllCustomers()
        queryset = Customer.objects.all()
        return queryset


class OrdersViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'ref'
    lookup_url_kwarg = 'ref'

    def get_queryset(self):
        queryset = Order.objects.all()
        search_param = self.request.query_params.get('customer', None)
        if search_param is not None:
            return Order.objects.filter(customerId__exact=str(search_param))
        return queryset
