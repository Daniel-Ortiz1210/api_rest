from rest_framework.views import APIView
from .models import Client
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ClientSerializer, ClientsSerializer
from rest_framework import status


# Create your views here.
class ClientsView(APIView):

    def get(self, request):
        '''
        Return all the clients in the DB if not a pk is provided, in contrary case returns the client with the pk
        '''
        clients = Client.objects.all()
        serializer = ClientsSerializer(clients, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):
        data = request.data
        serializer = ClientsSerializer(data=data)
        if serializer.is_valid():
            cient = Client.objects.create(**serializer.data)
            cient.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClientView(APIView):
    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
        