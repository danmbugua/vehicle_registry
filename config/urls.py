from django.conf.urls import include, url

urlpatterns = [
    url(r'^vehicles/', include('vehicles.urls', namespace='vehicles')),

]
