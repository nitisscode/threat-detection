from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from .views import UserAPIView, UserDetailAPIView, EventAPIView, EventDetailAPIView, AlertAPIView, AlertDetailAPIView

urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('users/', UserAPIView.as_view(), name='user_list'),
    path('users/<uuid:id>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('events/', EventAPIView.as_view(), name='event_list'),
    path('events/<uuid:id>/', EventDetailAPIView.as_view(), name='event_detail'),
    path('alerts/', AlertAPIView.as_view(), name='alert_list'),
    path('alerts/<uuid:id>/', AlertDetailAPIView.as_view(), name='alert_detail'),
]