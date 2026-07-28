from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import SystemAgent


@csrf_exempt
def register_agent(request):

    if request.method == "POST":

        data = json.loads(request.body)


        agent, created = SystemAgent.objects.update_or_create(

            agent_id=data["agent_id"],

            defaults={

                "hostname": data["hostname"],

                "ip_address": data["ip_address"],

                "operating_system": data["operating_system"],

                "status": "Online"

            }

        )


        return JsonResponse({

            "status":"success",

            "message":"Agent registered"

        })


    return JsonResponse({

        "error":"POST request required"

    })

def agents_view(request):

    agents = SystemAgent.objects.all()

    context = {
        "agents": agents
    }

    return render(request, "agents.html", context)