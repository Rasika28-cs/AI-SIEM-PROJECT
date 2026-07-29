from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def login_api(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    body = json.loads(request.body)

    username = body.get("username")
    password = body.get("password")

    print("Username:", username)
    print("Password:", password)

    user = authenticate(
        request,
        username=username,
        password=password
    )

    print("User:", user)

    if user is not None:
        login(request, user)
        return JsonResponse({"success": True})

    return JsonResponse(
        {
            "success": False,
            "message": "Invalid credentials"
        },
        status=401
    )


@csrf_exempt
def logout_api(request):

    logout(request)

    return JsonResponse({

        "success": True

    })