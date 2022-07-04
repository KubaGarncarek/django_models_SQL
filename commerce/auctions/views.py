from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listings, Comments, Categories


def index(request):
    return render(request, "auctions/index.html", {
        "listings" : Listings.objects.all()
    })

def create_listing(request):
    categories = Categories.objects.all()
    if request.method == "POST":
        user = request.user
        new_listing = Listings(title = request.POST['title'], description = request.POST['description'], bid = request.POST['starting_bid'], photo = request.POST['image'], highest_bidder = user.id, active=True,)
        new_listing.save()
        user.listing_owner.add(new_listing)
        user.save()
        category = request.POST['category']
        categories = Categories.objects.get(name = category)
        categories.listings.add(new_listing)
        categories.save()
        

        return HttpResponseRedirect(reverse("index"))
        
    return render(request, "auctions/create_listing.html", {
        "categories": categories
    })

def listing_page(request, listing_id):
    listing = Listings.objects.get(pk=listing_id)
    interested_users = listing.interested_users.all()
    listing_owner = listing.owner.all()
    comments = listing.comments.all()
    category = listing.category.all()
    return render(request, "auctions/listing_page.html", {
        "listing" : listing,
        "interested_users" : interested_users,
        "listing_owner" : listing_owner,
        "comments" : comments,
        "category" : category
    })

def watchlist(request, listing_id):
    listing = Listings.objects.get(pk=listing_id)
    user = request.user
    if request.user in listing.interested_users.all():
        user.watchlist.remove(listing)
    else:
        user.watchlist.add(listing)
    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))
    

def bidding(request, listing_id):
    listing = Listings.objects.get(pk=listing_id)
    user_bid = int(request.POST['bid'])
    if not user_bid > listing.bid:
        return render(request, "auctions/listing_page.html", {
            "listing": listing,
            "message": "must provide bid higher than actually bid"  
        })
    listing.bid = user_bid
    listing.highest_bidder = request.user.id
    print(listing.highest_bidder)
    listing.save()
    


    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))

def comment(request,listing_id):
    listing = Listings.objects.get(pk=listing_id)
    content = request.POST['comment']
    comment = Comments (content= content, listing = listing, owner= request.user    )
    comment.save()
    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))


    
def close_listing(request, listing_id):
    listing = Listings.objects.get(pk=listing_id)
    listing.active = False
    listing.save()
    return HttpResponseRedirect(reverse("listing_page", args=(listing_id,)))

def watchlist_page(request):
    user = request.user
    watchlist = user.watchlist.all()
    print(watchlist)
    return render(request, "auctions/watchlist.html", {
        "listings" : watchlist,
    })









def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
