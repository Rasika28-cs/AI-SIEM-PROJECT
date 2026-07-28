from django.shortcuts import render
from django.core.paginator import Paginator
from requests import request
from .models import SecurityLog
from agents.models import SystemAgent
from django.db.models import Q
from datetime import timedelta
from django.utils import timezone

def logs_view(request):

    logs = SecurityLog.objects.all().order_by("-timestamp")

    event_types = (
        SecurityLog.objects
        .values_list("event_type", flat=True)
        .distinct()
    )

    agents = SystemAgent.objects.all()

    search = request.GET.get("search", "")

    if search:
            logs = logs.filter(
            Q(message__icontains=search) |
            Q(event_type__icontains=search) |
            Q(source__icontains=search) |
            Q(agent__hostname__icontains=search)
        )

    severity = request.GET.get("severity", "")

    if severity:
        logs = logs.filter(severity=severity)

    event_type = request.GET.get("event_type", "")

    if event_type:
        logs = logs.filter(event_type=event_type)

    agent = request.GET.get("agent", "")

    if agent:
        logs = logs.filter(agent__id=agent)

    time_filter = request.GET.get("time", "")

    if time_filter == "today":
        logs = logs.filter(timestamp__date=timezone.now().date())

    elif time_filter == "24h":
        logs = logs.filter(
            timestamp__gte=timezone.now() - timedelta(hours=24)
        )

    elif time_filter == "7d":
        logs = logs.filter(
            timestamp__gte=timezone.now() - timedelta(days=7)
        )

    elif time_filter == "30d":
        logs = logs.filter(
            timestamp__gte=timezone.now() - timedelta(days=30)
        )

    paginator = Paginator(logs, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "logs.html", {
        "page_obj": page_obj,
        "search": search,
        "severity": severity,
        "time_filter": time_filter,
        "event_type": event_type,
        "event_types": event_types,
        "agent": agent,
        "agents": agents,
    })