from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from logs.models import SecurityLog
from alerts.models import Alert
from agents.models import SystemAgent


@login_required
def dashboard_view(request):

    total_logs = SecurityLog.objects.count()

    total_agents = SystemAgent.objects.count()

    total_alerts = Alert.objects.count()

    recent_logs = (
        SecurityLog.objects
        .select_related("agent")
        .order_by("-timestamp")[:10]
    )

    context = {
        "total_logs": total_logs,
        "total_agents": total_agents,
        "total_alerts": total_alerts,
        "recent_logs": recent_logs,
    }

    return render(request, "dashboard.html", context)