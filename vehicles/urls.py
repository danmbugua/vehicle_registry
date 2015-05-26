from django.conf.urls import patterns, url

from .views import (
    VehicleView,
    SingleVehicleView,
    OwnerView,
    SingleOwnerView
)

urlpatterns = patterns(
    '',
    url(r'^owners/(?P<id>\d+)/$', SingleOwnerView.as_view(),
        name='owner_detail'),
    url(r'^owners/$', OwnerView.as_view(),
        name='owners'),

    url(r'^vehicles/(?P<id>\d+)/$', SingleVehicleView.as_view(),
        name='vehicle_detail'),
    url(r'^vehicles/$', VehicleView.as_view(),
        name='vehicles'),
)
