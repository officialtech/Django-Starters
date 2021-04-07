# New Everything here

from django.urls import path
from .views import AppHomePage 

urlpatterns = [
    path('', AppHomePage.as_view(), name='app_home'),
]