from django.shortcuts import render
from django.core.paginator import Paginator
from requests import request
from .models import SecurityLog

def logs_view(request):

    logs = SecurityLog.objects.all().order_by("-timestamp")

    search = request.GET.get("search", "")

    if search:
        logs = logs.filter(message__icontains=search)

    severity = request.GET.get("severity", "")

    if severity:
        logs = logs.filter(severity=severity)

    paginator = Paginator(logs, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(request, "logs.html", {
        "page_obj": page_obj,
        "search": search,
        "severity": severity,
    })