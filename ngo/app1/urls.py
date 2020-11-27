from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('education', views.education, name='education'),
    path('adopt',views.adopt,name="adopt"),
    path('health',views.health,name="health"),
    path('disaster',views.disaster,name="dissaster"),
    path('volunteer',views.volunteer,name="volunteer"),
]
