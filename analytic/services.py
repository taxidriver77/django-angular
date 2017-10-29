import requests
from analytic.serializers import CustomerSerializer,OrderSerializer
from analytic.models import Customer,Order
from analytic.utils import UnixEpochDateTimeField

headers = {'x-api-key': '28f84ccd190145f5b9e460c565643873dbc8617f'}


def getHistory(id):
       url = 'http://bo.zelty.fr/app_api/1.0/customer/' + id + '/history'
       r = requests.get(url,headers=headers)
       history = r.json()
       print(url)
       for order in history['orders']:

           transactions = []
           contents = []

           for transaction in order['transactions']:
               aTransaction = {
                   'method': transaction['method'],
                   'price': transaction['price'],
                   'date': UnixEpochDateTimeField.epoch_to_datetime(transaction['date']),
               }
               #print(aTransaction)
               transactions.append(aTransaction)

           for content in order['content']:
               aContent = {
                   'name': content['name'],
                   'type': content['type'],
                   'item_id': content['item_id'],
                   'price': content['price'],
               }
               #print(aContent)
               contents.append(aContent)

           anOrder = {
               'ref': order['ref'],
               'customerId': id,
               'created_at': UnixEpochDateTimeField.epoch_to_datetime(order['created_at']),
               'transactions': transactions,
               'contents': contents,
           }

           serializer = OrderSerializer(data=anOrder)

           if serializer.is_valid(raise_exception=True):

               try:
                    obj = Order.objects.get(ref=anOrder['ref'])
               except Order.DoesNotExist:
                    serializer.save()
           else:
               serializer.errors()



def getAllCustomers():
    url = 'http://bo.zelty.fr/app_api/1.0/customers'
    r = requests.get(url,headers=headers)
    customers = r.json()
    print(url)
    for customer in customers['customers']:

       aCustomer = {
           'customerId': customer['id'],
           'name': customer['name'],
           'fname': customer['fname'],
           'nice_name': customer['nice_name'],
           'mail' : customer['mail'],
           'registration': UnixEpochDateTimeField.epoch_to_datetime(customer['registration']),
           'phone' : customer['phone']
       }

       serializer = CustomerSerializer(data=aCustomer)

       if serializer.is_valid(raise_exception=True):
           try:
                obj = Customer.objects.get(customerId=aCustomer['customerId'])
           except Customer.DoesNotExist:
                serializer.save()
                getHistory(str(customer['id']))
       else:
           serializer.errors()

