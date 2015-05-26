from rest_framework import serializers

from .models import Vehicle, Owner


class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
