from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.ProductList.as_view()),
    # url(r'(?P<pk>[a-z0-9]+)', views.ProductDetail.as_view()),
]
