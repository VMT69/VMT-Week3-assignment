from django.urls import path
from . import views

urlpatterns=[
    path('',views.indexPage,name="indexPage"),
    path('monday.html',views.mondayPage,name="mondayPage"),
    path('tuesday.html',views.tuesdayPage,name='tuesdayPage'),
    path('wednesday.html',views.wednesdayPage,name='wednesdayPage'),
    path('thursday.html',views.thursdayPage,name="thursdayPage"),
    path('friday.html',views.fridayPage,name="fridayPage"),
    path('saturday.html',views.saturdayPage,name="saturdayPage"),
    path('sunday.html',views.sundayPage,name="sundayPage")
]