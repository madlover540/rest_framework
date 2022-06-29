from dataclasses import fields
from rest_framework import serializers
from reseve.models import Custmer, Saloon, Reserve


class Saloon_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Saloon
        fields= '__all__'




class Reserve_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Reserve
        fields= '__all__'


class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Custmer
        fields= ['pk', 'reservation','name','phone_no']


