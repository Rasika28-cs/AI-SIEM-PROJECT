from django.db import models
from agents.models import SystemAgent


class SecurityLog(models.Model):

    agent = models.ForeignKey(SystemAgent, on_delete=models.CASCADE)

    timestamp = models.DateTimeField(auto_now_add=True)

    event_type = models.CharField(max_length=100)

    severity = models.CharField(max_length=20)

    source = models.CharField(max_length=100)

    category = models.CharField(max_length=100, blank=True)

    username = models.CharField(max_length=100, blank=True)

    message = models.TextField()

    raw_data = models.JSONField()

    def __str__(self):
        return f"{self.event_type} - {self.severity}"