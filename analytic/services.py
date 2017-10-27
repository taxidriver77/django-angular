import requests
from analytic.serializers import CustomerSerializer,OrderSerializer
from analytic.models import Customer
from analytic.utils import UnixEpochDateTimeField

headers = {'x-api-key': '28f84ccd190145f5b9e460c565643873dbc8617f'}

def getAllCustomers():
    url = 'http://bo.zelty.fr/app_api/1.0/customers'
    r = requests.get(url,headers=headers)
    customers = r.json()

    for customer in customers['customers']:

       aCustomer = {
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
                obj = Customer.objects.get(name=aCustomer['name'])
           except Customer.DoesNotExist:
                serializer.save()
       else:
           serializer.errors()



def getHistory(customerId):
       url = 'http://bo.zelty.fr/app_api/1.0/customer/' + customerId + '/history'
       r = requests.get(url,headers=headers)
       history = r.json()

       for order in history['orders']:

           transactions = []
           contents = []

           for transaction in order['transactions']:
               aTransaction = {
                   'method': transaction['method'],
                   'price': transaction['price'],
                   'date': UnixEpochDateTimeField.epoch_to_datetime(transaction['date']),
               }
               transactions.append(aTransaction)

           for content in order['contents']:
               aContent = {
                   'name': content['name'],
                   'type': content['type'],
                   'item_id': content['item_id'],
                   'price': content['price'],
               }
               contents.append(aContent)

           anOrder = {
               'created_at': UnixEpochDateTimeField.epoch_to_datetime(order['created_at']),
               'transactions': transactions,
               'contents': contents,
           }

           serializer = OrderSerializer(data=history)

           if serializer.is_valid(raise_exception=True):
               serializer.save()
               #try:
               #     obj = Order.objects.get(name=aCustomer['name'])
               #except Customer.DoesNotExist:
               #     serializer.save()
           else:
               serializer.errors()


#def getCustomer(customerId):
#        url = 'http://bo.zelty.fr/app_api/1.0/customer/' + customerId
#        r = requests.get(url,headers=headers)
#        customer = r.json()