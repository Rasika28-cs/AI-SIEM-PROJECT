from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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


    context = {
        "total_logs": total_logs,
        "total_agents": total_agents,
        "online_agents": online_agents,
        "total_alerts": total_alerts,
        "high_alerts": high_alerts,
        "recent_logs": recent_logs,
        "recent_alerts": recent_alerts,
    }


    return render(request, "dashboard.html", context)