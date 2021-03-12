from django.urls import path
from django.contrib import admin

from .views import (
    UserLoginAPIView
    )

urlpatterns = [
    path('login/', UserLoginAPIView.as_view(), name='login'),
    
]