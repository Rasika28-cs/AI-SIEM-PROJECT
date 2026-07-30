from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import Alert


def alerts_api(request):

    alerts = Alert.objects.select_related(
        "log",
        "log__agent"
    ).order_by("-created_time")

    search = request.GET.get("search", "")
    severity = request.GET.get("severity", "")
    status = request.GET.get("status", "")

    if search:
        alerts = alerts.filter(
            attack_type__icontains=search
        )

    if severity:
        alerts = alerts.filter(
            severity=severity
        )

    if status:
        alerts = alerts.filter(
            status=status
        )

    paginator = Paginator(alerts, 10)

    page = request.GET.get("page", 1)

    page_obj = paginator.get_page(page)

    data = list(

        page_obj.object_list.values(

            "id",
            "created_time",
            "attack_type",
            "severity",
            "status",
            "log__agent__hostname"

        )

    )

    return JsonResponse({

        "alerts": data,

        "pagination": {

            "page": page_obj.number,
            "pages": paginator.num_pages,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
            "next_page": page_obj.next_page_number() if page_obj.has_next() else None,
            "previous_page": page_obj.previous_page_number() if page_obj.has_previous() else None,

        }

    })