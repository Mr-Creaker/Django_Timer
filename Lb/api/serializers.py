from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Timer

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'gender', 'birth_date', 'password')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ['id', 'user', 'start_time', 'end_time', 'created_at']
        read_only_fields = ['user', 'created_at']  # user буде заповнюватись автоматично

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user  # Автоматично додаємо користувача
        return super().create(validated_data)
