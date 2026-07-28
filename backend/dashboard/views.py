from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Count
from logs.models import SecurityLog
from alerts.models import Alert
from agents.models import SystemAgent


@login_required
def dashboard_view(request):

    total_logs = SecurityLog.objects.count()

    total_agents = SystemAgent.objects.count()

    online_agents = SystemAgent.objects.filter(status="Online").count()

    total_alerts = Alert.objects.count()

    high_alerts = Alert.objects.filter(severity="HIGH").count()
    
    online_agents = SystemAgent.objects.filter(status="Online").count()

    high_alerts = Alert.objects.filter(severity="HIGH").count()

    recent_alerts = Alert.objects.order_by("-created_time")[:5]

    recent_logs = (
        SecurityLog.objects
        .select_related("agent")
        .order_by("-timestamp")[:10]
    )

    recent_alerts = (
        Alert.objects
        .order_by("-created_time")[:5]
    )

    logs_by_severity = (
        SecurityLog.objects
        .values("severity")
        .annotate(count=Count("id"))
    )

    alerts_by_status = (
        Alert.objects
        .values("status")
        .annotate(count=Count("id"))
    )


    context = {
        "total_logs": total_logs,
        "total_agents": total_agents,
        "online_agents": online_agents,
        "total_alerts": total_alerts,
        "high_alerts": high_alerts,
        "recent_logs": recent_logs,
        "recent_alerts": recent_alerts,
        "logs_by_severity": list(logs_by_severity),
        "alerts_by_status": list(alerts_by_status),
    }


    return render(request, "dashboard.html", context)