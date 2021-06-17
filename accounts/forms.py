from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,ReadOnlyPasswordHashField
from .models import (
    User,
)

class SpecialistSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email',"phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_specialist = True
        user.is_active = True
        if commit:
            user.save()
        return user

class PhysicianSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email',"phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_physician = True
        user.is_active = False
        if commit:
            user.save()
        return user

# class DoctorSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username','email',"phone_number", "password1", "password2")

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_doctor = True
#         user.is_active = False
#         if commit:
#             user.save()
#         return user
