import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Expense
from .parser import parse_message


@csrf_exempt
@require_POST
def webhook(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    message = data.get("message")
    phone = data.get("phone")

    if not message or not phone:
        return JsonResponse({"error": "missing fields"}, status=400)

    parsed = parse_message(message)

    if not parsed:
        return JsonResponse({"error": "Formato inválido"}, status=400)

    Expense.objects.create(
        phone=phone,
        name=parsed["name"],
        category=parsed["category"],
        amount=parsed["amount"],
    )

    return JsonResponse({"status": "ok"}, status=200)
