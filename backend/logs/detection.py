from datetime import timedelta

from django.utils import timezone

from alerts.models import Alert
from logs.models import SecurityLog


def detect_brute_force(log):

    if log.event_type != "LOGIN_FAILED":
        return

    one_minute_ago = timezone.now() - timedelta(minutes=1)

    failed_attempts = SecurityLog.objects.filter(
        agent=log.agent,
        event_type="LOGIN_FAILED",
        timestamp__gte=one_minute_ago
    ).count()

    if failed_attempts >= 5:

        Alert.objects.create(
            log=log,
            attack_type="Brute Force",
            severity="HIGH",
            status="OPEN"
        )