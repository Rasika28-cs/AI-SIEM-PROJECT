from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from .models import Alert


def alert_detail_api(request, pk):

    alert = get_object_or_404(
        Alert.objects.select_related("log", "log__agent"),
        pk=pk
    )

    return JsonResponse({

        "id": alert.id,
        "attack_type": alert.attack_type,
        "severity": alert.severity,
        "status": alert.status,
        "agent": alert.log.agent.hostname,
        "event_type": alert.log.event_type,
        "source": alert.log.source,
        "message": alert.log.message,
        "created_time": alert.created_time,

    })


@csrf_exempt
@require_http_methods(["POST"])
def update_status_api(request, pk):

    alert = get_object_or_404(Alert, pk=pk)

    body = json.loads(request.body)

    alert.status = body["status"]

    alert.save()

    return JsonResponse({
        "success": True
    })