from django.db import models
from logs.models import SecurityLog

class Alert(models.Model):
    STATUS_CHOICES = [
        ("Open", "Open"),
        ("Investigating", "Investigating"),
        ("Resolved", "Resolved"),
    ]

    log = models.ForeignKey(SecurityLog, on_delete=models.CASCADE)

    attack_type = models.CharField(max_length=100)

    severity = models.CharField(max_length=20)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Open"
    )

    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.attack_type