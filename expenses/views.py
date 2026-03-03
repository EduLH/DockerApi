import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model

from .models import Expense
from .parser import parse_message

User = get_user_model()


@csrf_exempt
@require_http_methods(["POST"])
def webhook(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    message = data.get("message")
    phone = data.get("phone")

    if not message or not phone:
        return JsonResponse({"error": "missing fields"}, status=400)

    user, _ = User.objects.get_or_create(phone=phone)

    parsed = parse_message(message)

    if not parsed:
        return JsonResponse({"error": "Formato inválido"}, status=400)

    Expense.objects.create(
        user=user,
        name=parsed["name"],
        category=parsed["category"],
        amount=parsed["amount"],
    )

    return JsonResponse({"status": "ok"}, status=200)