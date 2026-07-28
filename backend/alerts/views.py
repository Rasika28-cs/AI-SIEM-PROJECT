from django.shortcuts import render, get_object_or_404, redirect
from .models import Alert
from django.core.paginator import Paginator


def alerts_view(request):

    alerts = Alert.objects.all().order_by("-created_time")

    search = request.GET.get("search")
    severity = request.GET.get("severity")
    status = request.GET.get("status")

    if search:
        alerts = alerts.filter(attack_type__icontains=search)

    if severity:
        alerts = alerts.filter(severity=severity)

    if status:
        alerts = alerts.filter(status=status)

    paginator = Paginator(alerts, 10)
    page = request.GET.get("page")
    alerts = paginator.get_page(page)

    return render(request, "alerts.html", {
        "alerts": alerts
    })


def alert_detail(request, pk):

    alert = get_object_or_404(Alert, pk=pk)

    return render(request, "alert_detail.html", {
        "alert": alert
    })


def update_status(request, pk):

    alert = get_object_or_404(Alert, pk=pk)

    if request.method == "POST":

        alert.status = request.POST.get("status")
        alert.save()

    return redirect("alert_detail", pk=pk)