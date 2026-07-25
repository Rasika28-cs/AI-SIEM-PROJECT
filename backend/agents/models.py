from django.db import models


class SystemAgent(models.Model):
    agent_id = models.CharField(max_length=100, unique=True)
    hostname = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    operating_system = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Offline")
    last_seen = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hostname