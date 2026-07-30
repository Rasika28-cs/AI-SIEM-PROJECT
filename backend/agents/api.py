from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import timedelta
import json

from .models import SystemAgent


def agents_api(request):

    agents_data = []

    for agent in SystemAgent.objects.all():

        if timezone.now() - agent.last_seen <= timedelta(minutes=1):
            status = "Online"
        else:
            status = "Offline"

        agents_data.append({

            "id": agent.id,
            "hostname": agent.hostname,
            "agent_id": agent.agent_id,
            "ip_address": agent.ip_address,
            "operating_system": agent.operating_system,
            "status": status,
            "last_seen": agent.last_seen,

        })

    return JsonResponse({

        "agents": agents_data

    })



@csrf_exempt
def heartbeat_api(request):

    if request.method != "POST":

        return JsonResponse({
            "error": "POST only"
        }, status=405)

    body = json.loads(request.body)

    agent, created = SystemAgent.objects.get_or_create(

        agent_id=body["agent_id"],

        defaults={

            "hostname": body.get("hostname", "Unknown"),

            "ip_address": body.get("ip_address", "0.0.0.0"),

            "operating_system": body.get("operating_system", "Unknown"),

            "status": "Online"

        }

    )

    agent.hostname = body.get("hostname", agent.hostname)
    agent.ip_address = body.get("ip_address", agent.ip_address)
    agent.operating_system = body.get("operating_system", agent.operating_system)
    agent.status = "Online"
    agent.last_seen = timezone.now()

    agent.save()

    return JsonResponse({

        "success": True,

        "created": created

    })

