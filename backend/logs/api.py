from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta

from .models import SecurityLog
from agents.models import SystemAgent


def logs_api(request):

    logs = SecurityLog.objects.select_related("agent").order_by("-timestamp")

    event_types = list(
        SecurityLog.objects.values_list(
            "event_type",
            flat=True
        ).distinct()
    )

    agents = list(
        SystemAgent.objects.values(
            "id",
            "hostname"
        )
    )

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
        logs = logs.filter(
            timestamp__date=timezone.now().date()
        )

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

    page = request.GET.get("page", 1)

    page_obj = paginator.get_page(page)

    logs_data = list(

        page_obj.object_list.values(

            "timestamp",
            "agent__hostname",
            "event_type",
            "severity",
            "source",
            "message"

        )

    )

    return JsonResponse({

        "logs": logs_data,

        "event_types": event_types,

        "agents": agents,

        "search": search,
        "severity": severity,
        "event_type": event_type,
        "agent": agent,
        "time": time_filter,

        "pagination": {

            "page": page_obj.number,
            "pages": paginator.num_pages,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
            "next_page": page_obj.next_page_number() if page_obj.has_next() else None,
            "previous_page": page_obj.previous_page_number() if page_obj.has_previous() else None,

        }

    })