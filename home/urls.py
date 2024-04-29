from django.contrib import admin
from django.urls import path,include 
from home import views


urlpatterns = [

    path("register",views.registerPage,name='regsiter'),

    path("login",views.loginPage,name='login'),
    
    path("logout",views.logoutUser,name='logout'), 
    
    path("",views.index,name='home'),
    
    path("about",views.about,name='about'),
    
    path("services",views.services,name='services'),

    path("roomservice",views.roomservice,name='roomservice'),

    path("roombooking",views.roombooking,name='roombooking'),
    
    path("confirm",views.confirm,name='confirm'),

    path("payment",views.payment,name='payment'),

    path("contact",views.contact,name='contact'),
    path('feedback', views.feedback_view, name='feedback'),

]