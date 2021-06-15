from django.contrib import admin
from django.urls import path

from .views import (
    ApprovalListAPIView,
    ApprovalDeleteAPIView,
    ApprovalDetailAPIView,
    ApprovalUpdateAPIView,
    ApprovalCreateAPIView, 
	)

urlpatterns = [
    path('', ApprovalListAPIView.as_view(), name='Approvals'),
    path('Approval_new/', ApprovalCreateAPIView.as_view(), name='new'),
    path('<int:id>/Approval_detail/', ApprovalDetailAPIView.as_view(), name='detail'),
    path('<int:id>/edit/', ApprovalUpdateAPIView.as_view(), name='update'),
    path('<int:id>/store_delete/', ApprovalDeleteAPIView.as_view(), name="delete"),
]
