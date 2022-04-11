from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    image = models.ImageField(default='default.png',
                              upload_to='profile_images')

    def __str__(self):
        return f'{self.customer.username}-Profile'
