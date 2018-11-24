from django.conf.urls import include
from django.conf.urls import url

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
]