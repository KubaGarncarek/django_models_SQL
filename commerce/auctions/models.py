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

class Comments(models.Model):
    content = models.CharField(max_length= 128)
    listing = models.ForeignKey(Listings, blank = True, on_delete=models.CASCADE, related_name="comments")
    owner = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, related_name="owner")

class Categories(models.Model):
    name = models.CharField(max_length=20)
    listings = models.ManyToManyField(Listings, blank = True, null=True, related_name="category")
