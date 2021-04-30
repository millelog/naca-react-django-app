from django.shortcuts import render
from .models import Address
from .serializers import AddressSerializer
from rest_framework import generics

class AddressListCreate(generics.ListCreateAPIView):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer


# Create your views here.
