import json
import traceback
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from agents.models import SystemAgent
from logs.models import SecurityLog
from logs.detection import detect_brute_force


@csrf_exempt
def upload_log(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "POST request required"},
            status=405
        )

    try:

        data = json.loads(request.body)

        required_fields = [
            "agent",
            "type",
            "severity",
            "message"
        ]

        for field in required_fields:
            if field not in data:
                return JsonResponse(
                    {
                        "error": f"Missing field: {field}"
                    },
                    status=400
                )

        agent = SystemAgent.objects.get(
            agent_id=data["agent"]
        )

        new_log = SecurityLog.objects.create(
            agent=agent,
            event_type=data["type"],
            severity=data["severity"],
            source=data.get("source", "SIEM Agent"),
            message=data["message"],
            raw_data=data
        )

        detect_brute_force(new_log)

        return JsonResponse({
            "status": "success",
            "message": "Log uploaded successfully"
        }, status=201)

    except SystemAgent.DoesNotExist:

        return JsonResponse({
            "error": "Agent not found"
        }, status=404)

    except Exception as e:

        traceback.print_exc()

        return JsonResponse({
            "error": str(e)
        }, status=400)