from rest_framework.serializers import (
        HyperlinkedIdentityField,
        ModelSerializer,
        SerializerMethodField,
        )

from accounts.api.serializers import UserDetailSerializer
# from medicine.api.serializers import ProductSerializer
from patients.models import Patient
# from .serializers import PostSerializer
from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers
from django.db import models
from django.conf import settings


class PatientCreateUpdateSerializer(ModelSerializer):
    user 		   = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete = models.CASCADE)
    class Meta:
        model = Patient
        fields = [
            # 'id',
            'user',
            'patient_name',
            'patient_id',
            'heart_rate',
            'respiratory_rate',
            'patient_history',
            'recommended_diagnosis',
            'temperature',
            'blood_pressure',
        ]


patient_detail_url = HyperlinkedIdentityField(
        view_name='patients-api:detail',
        lookup_field='id'#or primary key <pk>
    )

class PatientDetailSerializer(ModelSerializer):
    url = patient_detail_url
    user = UserDetailSerializer(read_only=True)
    # store_logo = SerializerMethodField()
    class Meta:
        model = Patient
        fields = [
            'url',
            'id',
            'patient_name',
            'patient_id',
            'heart_rate',
            'respiratory_rate',
            'temperature',
            'blood_pressure',
            'patient_history',
            'recommended_diagnosis',
            'user',
            'active',
            'updated',
            'timestamp'
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)

    # def get_store_logo(self, obj):
    #     try:
    #         store_logo = obj.store_logo.url
    #     except:
    #         store_logo = None
        
    #     return store_logo

class PatientListSerializer(ModelSerializer):
    url = patient_detail_url
    user    =   UserDetailSerializer(read_only=True)
    delete_url = HyperlinkedIdentityField(
        view_name='patients-api:delete',
        lookup_field='id'#or primary key <pk>
    )
    class Meta:
        model = Patient
        fields = [
            'url',
            'user',
            'id',
            'delete_url',
            'patient_name',
            'patient_id',
            'heart_rate',
            'patient_history',
            'recommended_diagnosis',
            'respiratory_rate',
            'temperature',
            'blood_pressure',
            'active',
            'updated',
            'timestamp'
        ]
    
    # def get_user(self, obj):
    #     return str(obj.user.username)