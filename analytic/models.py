# coding=utf-8
from datetime import datetime
from mongoengine import Document, StringField, ListField,DateTimeField,\
    EmbeddedDocumentField,IntField,LongField,EmbeddedDocument
from analytic.utils import UnixEpochDateTimeField


class Transaction(EmbeddedDocument):
    method = StringField(max_length=20)
    price = LongField(min_value=None)
    date = UnixEpochDateTimeField()


class Content(EmbeddedDocument):
    name = StringField(max_length=50)
    type = StringField(max_length=50)
    item_id = LongField(min_value=None)
    price = LongField(min_value=None)


class Order(Document):
    ref = LongField(min_value=None)
    customerId = LongField(min_value=None)
    created_at = UnixEpochDateTimeField()
    transactions = ListField(EmbeddedDocumentField(Transaction))
    contents = ListField(EmbeddedDocumentField(Content))



class Customer(Document):
    customerId = LongField(min_value=None)
    name = StringField(max_length=50)
    fname = StringField(max_length=50)
    nice_name = StringField(max_length=100)
    mail = StringField(null=True)
    registration = UnixEpochDateTimeField()
    phone = StringField(max_length=100,null=True)


