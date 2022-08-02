from rest_framework import serializers
from .models import Client

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['username', 'name', 'password', 'email', 'age', 'height', 'weight', 'geb', 'imc', 'created_at']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'