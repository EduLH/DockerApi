import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    try:
        data = json.loads(request.body)
        user = User.objects.create(
            phone=data["phone"],
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            email=data.get("email", ""),
        )
        return JsonResponse(
            {
                "id": str(user.id),
                "phone": user.phone,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            },
            status=201,
        )
    except KeyError:
        return JsonResponse({"error": "Missing fields"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@require_http_methods(["GET"])
def list_users(request):
    users = list(
        User.objects.values(
            "id", "phone", "first_name", "last_name", "email"
        )
    )
    return JsonResponse(users, safe=False)


@require_http_methods(["GET"])
def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return JsonResponse(
        {
            "id": str(user.id),
            "phone": user.phone,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }
    )


@csrf_exempt
@require_http_methods(["PUT"])
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    try:
        data = json.loads(request.body)

        user.phone = data.get("phone", user.phone)
        user.first_name = data.get("first_name", user.first_name)
        user.last_name = data.get("last_name", user.last_name)
        user.email = data.get("email", user.email)

        user.save()

        return JsonResponse(
            {
                "id": str(user.id),
                "phone": user.phone,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            }
        )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return JsonResponse({"status": "deleted"}, status=204)