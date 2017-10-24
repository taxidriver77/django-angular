from rest_framework.response import Response
from rest_framework import status
from rest_framework_mongoengine import serializers
from scrumboard.models import List, Card
import pprint

class CardSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class ListSerializer(serializers.DocumentSerializer):
    cards = CardSerializer(read_only = False, many = True)
    class Meta:
        model = List
        fields = '__all__'
        #depth = 3
        #fields = ('id','name','cards')
        #extra_kwargs = {'cards': {'read_only': False, 'required': True}} #very important


    def update(self, instance, validated_data):
        '''
        instance.name = validated_data.pop('name')
        #instance.cards = validated_data['cards']
        #instance.save()
        items = validated_data.get('cards')
        pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(items)

        for item in items:
            #pp.pprint(item)
            cardObj = Card.objects.create()
            for key, value in item.items():
                if key == 'title':
                    cardObj.title = validated_data.get(value)
                if key == 'description':
                    cardObj.description = validated_data.get(value)
                if key == 'story_points':
                    cardObj.story_points = validated_data.get(value)
                if key == 'business_value':
                    cardObj.business_value = validated_data.get(value)
                if key == 'list':
                    cardObj.list = validated_data.get(value)
            cardObj.save()


        #instance.cards = items
        instance.save()
        pp.pprint(instance.cards)
        '''
        instance = self.recursive_save(validated_data, instance)
        return instance

'''
    def update(self, instance, validated_data):
        # Update the  instance
        instance.name = validated_data['name']
        instance.cards = validated_data['cards']
        instance.save()

        # Create or update owner
        for aCard in validated_data['cards']:
            ownerObj = Card.objects.get(pk=item['id'])
            if ownerObje:
                ownerObj.some_field=item['some_field']
                ....fields...
            else:
               ownerObj = Owner.create(car=instance,**aCard)
            ownerObj.save()

        return instance

    def partial_update(self, instance, validated_data):
        #print  'this - here'
        list = List.objects.get(pk=instance.id)
        List.objects.filter(pk=instance.id)\
                           .update(**validated_data)
        return list
'''



