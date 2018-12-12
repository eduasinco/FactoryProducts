from rest_framework import serializers
from products.models import Product, Material, Allergen


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('name', 'quantity', 'units')


class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ('name',)


class ProductSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True, read_only=True)
    allergens = AllergenSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
