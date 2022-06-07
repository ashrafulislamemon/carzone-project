from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='homepage'),
    path('about',views.about,name='aboutpage'),
    path('services',views.services,name='servicespage'),
    path('contact',views.contact,name='contactpage'),

   

]
