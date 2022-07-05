from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listings/<int:listing_id>", views.listing_page, name="listing_page"),
    path("watchlist/<int:listing_id>", views.watchlist, name="watchlist"),
    path("bidding/<int:listing_id>", views.bidding, name="bidding"),
    path("close_listing/<int:listing_id>", views.close_listing, name="close_listing"),
    path("comment/<int:listing_id>", views.comment, name="comment"),
    path("watchlist_page", views.watchlist_page, name="watchlist_page"),
    path("categories", views.categories, name="categories"),
    path("listings_from_category/<int:category_id>", views.listings_from_category, name="listings_from_category"),
]  
urlpatterns += staticfiles_urlpatterns()
