from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('open_signup',views.open_signup,name="open_signup"),
    path('open_signin',views.open_signin,name="open_signin"),
    path('signup',views.signup,name="signup"),
]