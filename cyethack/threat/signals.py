from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event, Alert, Severity

@receiver(post_save, sender=Event)
def create_alert(sender, instance, created, **kwargs):
    if created:
        if instance.severity in ["high", "critical"]:
            Alert.objects.create(event=instance, status="open")
