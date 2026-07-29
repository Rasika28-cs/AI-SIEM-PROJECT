from django.http import JsonResponse

from logs.models import SecurityLog
from alerts.models import Alert
from agents.models import SystemAgent

from django.db.models import Count


def dashboard_api(request):

    data = {

        "total_logs":
            SecurityLog.objects.count(),

        "total_alerts":
            Alert.objects.count(),

        "online_agents":
            SystemAgent.objects.filter(
                status="Online"
            ).count(),

        "high_alerts":
            Alert.objects.filter(
                severity="HIGH"
            ).count(),


        "recent_alerts":
            list(
                Alert.objects
                .order_by("-created_time")
                .values(
                    "attack_type",
                    "severity",
                    "status",
                    "created_time"
                )[:5]
            ),


        "recent_logs":
            list(
                SecurityLog.objects
                .select_related("agent")
                .order_by("-timestamp")
                .values(
                    "timestamp",
                    "agent__hostname",
                    "event_type",
                    "severity"
                )[:10]
            ),


        "logs_by_severity":
            list(
                SecurityLog.objects
                .values("severity")
                .annotate(
                    count=Count("id")
                )
            ),


        "alerts_by_status":
            list(
                Alert.objects
                .values("status")
                .annotate(
                    count=Count("id")
                )
            )

    }


    return JsonResponse(data)