from django.contrib.auth.models import AbstractUser
from django.db import models




class Listings(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 64)
    starting_bid = models.FloatField()

    # TODO 
    # adding images and category
    # image = models.ImageField

class User(AbstractUser):
    watchlist = models.ManyToManyField(Listings, blank = True, related_name="interested_users")