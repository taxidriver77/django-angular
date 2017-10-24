from mongoengine import *
from mongoengine import DynamicDocument,Document,EmbeddedDocument,EmbeddedDocumentListField,EmbeddedDocumentField,ListField,ObjectIdField, ReferenceField, StringField,IntField,PULL,CASCADE


class Card(Document):
    title = StringField(max_length=100)
    description = StringField(null = True,blank = True, help_text="Here is a description")
    #list = ReferenceField(List, required = True, reverse_delete_rule=CASCADE)
    list = ObjectIdField(required=False)
    story_points = IntField(null = True,blank = True)
    business_value =IntField(null = True,blank = True)

class List(Document):
    name = StringField(max_length=50)
    cards = ListField(ReferenceField(Card,read_only = False,required =True,reverse_delete_rule=PULL))



'''
class Card(EmbeddedDocument):
    title = StringField(max_length=100)
    description = StringField(blank = True, help_text="Here is a description")
    #list = ReferenceField(List, required = True, reverse_delete_rule=CASCADE)
    #list = ObjectIdField(required=False)
    story_points = IntField(null = True,blank = True)
    business_value =IntField(null = True,blank = True)

class List(Document):
    name = StringField(max_length=50)
    cards = EmbeddedDocumentListField(Card,required= False)

'''

















