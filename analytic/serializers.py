# _*_ coding: utf-8 _*_
from rest_framework_mongoengine import serializers
from analytic.models import Customer,Order,Transaction,Content


class CustomerSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Customer
        depth = 1
        fields = ('customerId','name', 'fname', 'nice_name', 'mail', 'registration','phone')
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
        fields = ('ref','customerId','created_at', 'transactions', 'contents')

    def create(self, validated_data):

        transactions = validated_data.pop('transactions')
        contents = validated_data.pop('contents')
        order = Order.objects.create(**validated_data)

        for transaction_data in transactions:
            order.transactions.append(Transaction(**transaction_data))

        for content_data in contents:
            order.contents.append(Content(**content_data))

        order.save()
        return order


