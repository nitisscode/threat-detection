from django.urls import path
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Threat Detection API",
        default_version="v1",
        description="Security Event Ingestion and Alert Management System",
        contact=openapi.Contact(email="support@example.com"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]
