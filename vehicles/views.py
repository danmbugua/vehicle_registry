from rest_framework import generics

from .models import Vehicle, Owner
from .serializers import VehicleSerializer, OwnerSerializer


class VehicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_fields = ('make', )
    ordering_fields = ('number_plate', 'make', )


class SingleVehicleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class OwnerView(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    ordering_fields = ('id_number', 'fisst_name', )


class SingleOwnerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
