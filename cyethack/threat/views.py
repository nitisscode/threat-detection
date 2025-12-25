from django.shortcuts import render
from rest_framework import views, generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .permissions import IsAdmin
from .serializers import UserSerializer, EventSerializer, AlertSerializer
from .models import User, Event, Alert
from .filters import AlterFilter, EventFilter
# Create your views here.

class UserAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def get_permissions(self):
    #     if self.request.method == 'POST':
    #         return [IsAdmin()]
    #     return super().get_permissions()

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


class EventAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class EventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    lookup_field = 'id'

class AlertAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AlertSerializer
    # filter_backends = [DjangoFilterBackend, SearchFilter]
    # filterset_class = AlterFilter
    search_fields = ['event__source', 'event__event_type', 'event__severity', 'status']
    queryset = Alert.objects.all()

class AlertDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AlertSerializer
    queryset = Alert.objects.all()
    lookup_field = 'id'


    def get_permissions(self):
        if self.request.method in ["PUT", "PATCh", "DELETE"]:
            return [IsAdmin()]
        return super().get_permissions()






