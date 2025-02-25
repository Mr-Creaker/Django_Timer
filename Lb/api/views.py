from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from .models import Timer
from .serializers import UserSerializer, TimerSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class TimerViewSet(viewsets.ModelViewSet):
    queryset = Timer.objects.all()
    serializer_class = TimerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Додаємо користувача при створенні
    @action(detail=False, methods=['get'])
    def active_timers(self, request):
        """ Отримати всі активні таймери (які ще не закінчилися) """
        active_timers = Timer.objects.filter(end_time__gt=now())
        serializer = self.get_serializer(active_timers, many=True)
        return Response(serializer.data)