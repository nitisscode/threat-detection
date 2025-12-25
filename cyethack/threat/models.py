
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class CoreAbstractModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#         return self.create_user(email, password, **extra_fields)

class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    ANALYST = 'analyst', 'Analyst'

class User(CoreAbstractModel, AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.ANALYST)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []


    def __str__(self):
        return self.email

class Severity(models.TextChoices):
    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "HIgh"
    CRITICAL = "critical", "Critical"

class Event(CoreAbstractModel):
    source = models.CharField(max_length=100)
    event_type = models.CharField(max_length=50, help_text="e.g., intrusion, malware, anomaly")
    severity = models.CharField(max_length=10, choices=Severity.choices, default=Severity.LOW)
    description = models.TextField()

    def __str__(self):
        return self.source

class Status(models.TextChoices):
    OPEN = "open", "Open"
    ACKNOWLEDGED = "acknowledged", "Acknowledged"
    RESOLVED = "resolved", "Resolved"

    
class Alert(CoreAbstractModel):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.OPEN)

    def __str__(self):
        return f"Alert for {self.event.source} - {self.status}"