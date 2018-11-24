from django.db import models

ALLERGENS = (
    ('cereals', 'cereals'),
    ('nuts', 'nuts'),
    ('daily', 'daily'),
    ('eggs', 'eggs'),
    ('sesame', 'sesame'),
)


class Factory(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


class Tag(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    word = models.CharField(max_length=35)

    def __unicode__(self):
        return self.word


class Product(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    family = models.CharField(max_length=100, blank=True, default='')
    tags = models.ManyToManyField(Tag, related_name='product')
    allergens = models.CharField(max_length=100, blank=True, null=True, choices=ALLERGENS)
    customer = models.CharField(max_length=100, blank=True, default='')
    colour = models.CharField(max_length=100, blank=True, default='')
    range = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name


class Materials(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    quantity = models.FloatField()
    units = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name
