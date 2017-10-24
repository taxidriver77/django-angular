#from django.shortcuts import render
from rest_framework_mongoengine.viewsets import ModelViewSet
from rest_framework import permissions, status, parsers, renderers
from rest_framework.response import Response
from scrumboard.models import Card,List
from scrumboard.serializers import ListSerializer,CardSerializer


from django.shortcuts import Http404


class CardViewSet(ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    #lookup_field = 'id'
    #parser_classes = (parsers.JSONParser,)
    #renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    #permission_classes = (IsAuthenticated,)

'''
    def get_queryset(self):
        queryset = Card.objects.all()
        return queryset

    def create(self, request, **kwargs):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            card = serializer.save()
            return Response({"id": str(card.title)}, status=status.HTTP_201_CREATED, content_type="application/json")
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        card = self.get_object()
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            card = serializer.save()
            #update_session_auth_hash(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({
                    'status': 'Failed',
                    'message': 'Update failed with submitted data'
                }, status=status.HTTP_400_BAD_REQUEST)
'''




class ListViewSet(ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    #lookup_field = 'id'
    #parser_classes = (parsers.JSONParser,)
    #renderer_classes = (renderers.JSONRenderer,)
    queryset = List.objects.all()
    serializer_class = ListSerializer
    #permission_classes = (IsAuthenticated,)
'''
    def get_object(self):
        try:
            list = List.objects(id=self.kwargs['id'])[0]
        except IndexError:
            raise Http404
        #self.check_object_permissions(self.request, list)
        return list

    def update(self, request, *args, **kwargs):
        list = self.get_object()
        serializer = ListSerializer(list, data=request.data)
        if serializer.is_valid():
            list = serializer.save()
            #update_session_auth_hash(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({
                    'status': 'Failed',
                    'message': 'Update failed with submitted data'
                }, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk=None):
        serializer = ListSerializer(request.user, data=request.data, partial=True)
        serializer.save()
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)



    def get_serializer_class(self):
        """
        Checks if request is authenticated and if not
        send user's info without email field
        :return: Postserializer or PostSerializerNonAuth
        """
        return ListSerializer

    def list(self, request, *args, **kwargs):
        if request.GET.get('id'):
            ds = self.get_serializer_class()(List.objects().all(), many=True)
        else:
            ds = self.get_serializer_class()(self.get_queryset(), many=True)

        return Response(ds.data)

    def create(self, request, **kwargs):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            list = serializer.save()
            return Response({"id": str(list.name)}, status=status.HTTP_201_CREATED, content_type="application/json")
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)
'''







