from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('adopt',views.adopt,name="adopt"),
    path('donation',views.donation,name="donation"),
    path('events',views.events,name="Events"),
    path('volunteer',views.volunteer,name="volunteer"),
    path('vollist',views.vollist,name="vollist")
]
