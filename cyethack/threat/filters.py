from django_filters import FilterSet
from . models import Event, Alert 
from django_filters import filters
class AlterFilter(FilterSet):
    severity = filters.CharFilter(field_name="event__severity", lookup_expr='icontains')
    status = filters.CharFilter(field_name="status", lookup_expr='icontains')
    class Meta:
        model = Alert
        fields = ['severity', 'status']

class EventFilter(FilterSet):
    severity = filters.CharFilter(field_name="severity", lookup_expr='icontains')
    event_type = filters.CharFilter(field_name="event_type", lookup_expr='icontains')
    class Meta:
        model = Event
        fields = ['severity', 'event_type']

