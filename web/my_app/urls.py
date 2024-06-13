from django.urls import path
from my_app import views


urlpatterns = [
    path('',views.index),
    path('register/',views.regis),
    # path('aboutus/',views.about),
    # path('aboutus/<str:aboutusid>',views.aboutus),
    # dynamic address
    path('home/',views.home),
] 