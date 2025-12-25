
from rest_framework import serializers

from .models import User, Event, Alert

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "role", "password", "created_at", "updated_at"]
        extra_kwargs ={
            "password": {"write_only": True}
        }
        #write_only_fields = ["password"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
        
        instance.save()
        return instance


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "source", "event_type", "severity", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ["id", "event", "status", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]



    