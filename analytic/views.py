from django.shortcuts import render
import services
from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework import permissions, status, parsers, renderers, generics
from rest_framework.response import Response
from analytic.models import Customer,Order
from analytic.serializers import CustomerSerializer,OrderSerializer


class CustomersViewSet(ModelViewSet):
    #parser_classes = (parsers.JSONParser,)
    #renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CustomerSerializer

    def get_queryset(self):
        services.getAllCustomers()
        queryset = Customer.objects.all()
        return queryset



class OrdersViewSet(ModelViewSet):
    #parser_classes = (parsers.JSONParser,)
    #renderer_classes = (renderers.JSONRenderer,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        services.getHistory()
        queryset = Order.objects.all()
        return queryset