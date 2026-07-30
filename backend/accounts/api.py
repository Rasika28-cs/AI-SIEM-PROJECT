from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json

from .forms import UserRegistrationForm
from .models import Profile



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

    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    logout(request)

    return JsonResponse({
        "success": True
    })



@csrf_exempt
def register_api(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)

    body = json.loads(request.body)

    form = UserRegistrationForm(body)

    if form.is_valid():

        user = form.save()

        Profile.objects.create(
            user=user,
            role=form.cleaned_data["role"]
        )

        login(request, user)

        return JsonResponse({
            "success": True
        })

    return JsonResponse({
        "success": False,
        "errors": form.errors
    }, status=400)