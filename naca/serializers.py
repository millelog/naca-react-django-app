from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'address', 'city', 'state', 'zipcode', 'msacode', 'medianIncome', 'geocode', 'isNacaApproved' )
