from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from approvals.models import Approval
# from .serializers import PostSerializer
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class ApprovalCreateUpdateSerializer(ModelSerializer):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    approvedby 	   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, blank = True)
    class Meta:
        model = Approval
        fields = [
            # 'id',
            'user',
            'approvedby',
            'status',
        ]


patient_detail_url = HyperlinkedIdentityField(
        view_name='approvals-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class ApprovalDetailSerializer(ModelSerializer):
    url = patient_detail_url
    user = UserDetailSerializer(read_only=True)
    # store_logo = SerializerMethodField()
    class Meta:
        model = Approval
        fields = [
            'url',
            'id',
            'user',
            'status',
            'approvedby',
            'updated',
            'timestamp'
        ]

class ApprovalListSerializer(ModelSerializer):
    url = patient_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='approvals-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = Approval
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'status',
            'approvedby',
            'updated',
            'timestamp'
        ]