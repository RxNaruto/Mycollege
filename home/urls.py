from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path('signup/',views.signup,name='signup'),
    path('explore/',views.explore,name='explore'),
    path('projectsfn/', views.projectsfn, name='projectsfn'),
    
    #path('events/',views.events,name='events'),
    #path('hackathons/',views.hackathons,name='hackathons'),
]
