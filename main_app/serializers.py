from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = [
            "User_Name",
            "E_mail",
            "Confirm_mail",
        ]
        extra_kwords = {
            # not needed now
        }