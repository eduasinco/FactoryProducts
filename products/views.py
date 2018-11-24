from rest_framework import generics
from products.models import Product, Factory
from products.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

factorySerializer = {
    1: ProductSerializerFood,
    3: ProductSerializerTextile
}


class ProductList(APIView):

    def get(self, request):
        factory_name = request.META['HTTP_X_API_KEY']
        factory = Factory.objects.get(name=factory_name)
        products = Product.objects.filter(factory=factory.id)
        serializer = factorySerializer[factory.id](products, many=True)
        return Response(serializer.data)

    def post(self, request):
        factory_name = request.META['HTTP_X_API_KEY']
        factory = Factory.objects.get(name=factory_name)
        data = {}
        for k in request.data:
            data[k] = request.data[k]
        data['factory'] = factory.id
        serializer = factorySerializer[factory.id](data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
