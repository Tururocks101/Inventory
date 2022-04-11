from django.db import models

# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),

)

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=30, choices= CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.name}'