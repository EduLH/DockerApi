import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Expense
from .parser import parse_message


@csrf_exempt
def webhook(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=400)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    message = data.get("message")
    phone = data.get("phone")

    parsed = parse_message(message)

    if not parsed:
        return JsonResponse({"error": "Formato inválido"}, status=400)

    Expense.objects.create(
        phone=phone,
        name=parsed["name"],
        category=parsed["category"],
        amount=parsed["amount"],
    )

    return JsonResponse({"status": "ok"})
