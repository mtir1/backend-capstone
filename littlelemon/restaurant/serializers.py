from rest_framework import serializers
from .models import Booking, Menu

class MenuSerializer(serializers.ModelSerializer):
    pass

class BookingSerializer(serializers.ModelSerializer):
    model = Booking
    fields = "__all__"