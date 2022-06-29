from ast import Delete
from django.http import JsonResponse, Http404
from django.shortcuts import render
from reseve import serializers
from reseve.models import Custmer, Reserve, Saloon
from rest_framework.decorators import api_view
from reseve.serializers import Customer_Serializer,Reserve_Serializer,Saloon_Serializer
from rest_framework import status, filters
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.



# withou RESTFRAMEWORK and no model query FBV

def no_rest_no_model (request):
    guest = [
        {
            'id':1,
            'name':'omer',
            'mobile':'0912320690'
        },{
            'id':3,
            'name':'ahmed',
            'mobile':'0918329939'
        }
    ]

    return JsonResponse(guest, safe=False)

# norest but model

def no_rest_but_model (request):
        data = Custmer.objects.all()
        response = {
            'customers': list(data.values('name', 'phone_no'))
        }

        return JsonResponse(response)


#django rest framework fbv

@api_view(['GET','POST'])
def fbv_list(request):
    if request.method  == 'GET':
        customers = Custmer.objects.all()
        serializer = Customer_Serializer(customers, many=True)
        return Response(serializer.data)

    elif request.method  == 'POST':
        serializer = Customer_Serializer(data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status = status.HTTP_201_CREATED)

        return Response (serializer.data, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def fbv_pk(request, pk):


    
    try:
        customers = Custmer.objects.get(pk = pk)
    except Custmer.DoesNotExists:
        return Response (status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        
        serializer = Customer_Serializer(customers, )
        return Response(serializer.data)

    elif request.method  == 'PUT':
        serializer = Customer_Serializer(customers, data = request.data )
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)

        return Response (serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method  == 'DELETE':
        customers.delete()
        
    
        return Response ( status = status.HTTP_404_NOT_FOUND)

#cbv get post


class CBV_list(APIView):
    def get(self, request):
        customers = Custmer.objects.all()
        serializer = Customer_Serializer(customers, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Customer_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class Cbv_pk(APIView):
    def get_object(self, pk):
        try:
            return Custmer.objects.get(pk=pk)
        except Custmer.DoesNotExist:
            raise Http404

    def get(self,request , pk):
        Custmer = self.get_object(pk)
        serializer = Customer_Serializer(Custmer) 
        return Response(serializer.data)
    
    def put(self, request, pk,format=None):
        Custmer = self.get_object(pk)
        serializer = Customer_Serializer(Custmer, data= request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, pk,format=None):
        Custmer = self.get_object(pk)
        Custmer.delete()
        return Response (status=status.HTTP_404_NOT_FOUND)
        




    
    






        
