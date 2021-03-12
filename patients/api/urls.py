from django.contrib import admin
from django.urls import path

from .views import (
    PatientListAPIView,
    PatientDeleteAPIView,
    PatientDetailAPIView,
    PatientUpdateAPIView,
	)

urlpatterns = [
    path('', PatientListAPIView.as_view(), name='patients'),
    # path('patient_new/', PatientUpdateAPIView.as_view(), name='new'),
    path('<int:id>/patient_detail/', PatientDetailAPIView.as_view(), name='detail'),
    path('<int:id>/edit/', PatientUpdateAPIView.as_view(), name='update'),
    path('<int:id>/store_delete/', PatientDeleteAPIView.as_view(), name="delete"),
]
