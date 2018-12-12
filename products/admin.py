from django.contrib import admin
from models import Product, Material, Allergen
from FactoryProducts.admin import *

admin.site.register(Product)
admin.site.register(Material)
admin.site.register(Allergen)
