from django.http import JsonResponse

from .models import SystemAgent


def agents_api(request):

    agents = list(

        SystemAgent.objects.values(

            "id",
            "hostname",
            "agent_id",
            "ip_address",
            "operating_system",
            "status",
            "last_seen"

        )

    )

    return JsonResponse({

        "agents": agents

    })