from django.db import models


class Factory(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


class User(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


class Allergen(models.Model):
    name = models.CharField(max_length=35)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    family = models.CharField(max_length=100, blank=True, default='')
    tags = models.TextField()
    allergens = models.ManyToManyField(Allergen, related_name='allergens')
    customer = models.CharField(max_length=100, blank=True, default='')
    colour = models.CharField(max_length=100, blank=True, default='')
    range = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


class Material(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='materials')
    name = models.CharField(max_length=100, blank=True, default='')
    quantity = models.FloatField()
    units = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name
