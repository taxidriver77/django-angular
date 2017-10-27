# _*_ coding: utf-8 _*_
from rest_framework_mongoengine import serializers
from analytic.models import Customer,Order,Transaction,Content


class CustomerSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Customer
        depth = 1
        fields = ('name', 'fname', 'nice_name', 'mail', 'registration','phone')
        #read_only_fields = ('id', 'created_at', 'updated_at')


class TransactionSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Transaction

class ContentSerializer(serializers.EmbeddedDocumentSerializer):
    class Meta:
        model = Content

class OrderSerializer(serializers.DocumentSerializer):
    transactions = TransactionSerializer(many=True)
    contents = ContentSerializer(many=True)

    class Meta:
        model = Order
        depth = 2
        fields = ('created_at', 'transactions', 'contents')

