from django.contrib.auth.models import AbstractUser
from django.db import models

class Listings(models.Model):
    
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 64)
    bid = models.FloatField()
    photo = models.CharField(max_length = 128)
    highest_bidder = models.IntegerField()
    active = models.BooleanField()

    # TODO 
    # adding images and category
    # image = models.ImageField

class User(AbstractUser):
    watchlist = models.ManyToManyField(Listings, blank = True, related_name="interested_users")
    listing_owner = models.ManyToManyField(Listings, blank = True, related_name="owner")

