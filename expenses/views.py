import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404

from .models import Expense, User
from .parser import parse_message


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

    # Check if user exists
    try:
        user = User.objects.get(phone=phone)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

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


@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    try:
        data = json.loads(request.body)
        user = User.objects.create(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        return JsonResponse({'id': user.id, 'name': user.name, 'email': user.email, 'phone': user.phone}, status=201)
    except KeyError:
        return JsonResponse({'error': 'Missing fields'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@require_http_methods(["GET"])
def list_users(request):
    users = list(User.objects.values('id', 'name', 'email', 'phone'))
    return JsonResponse(users, safe=False)


@require_http_methods(["GET"])
def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return JsonResponse({'id': user.id, 'name': user.name, 'email': user.email, 'phone': user.phone})


@csrf_exempt
@require_http_methods(["PUT"])
def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    try:
        data = json.loads(request.body)
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.phone = data.get('phone', user.phone)
        user.save()
        return JsonResponse({'id': user.id, 'name': user.name, 'email': user.email, 'phone': user.phone})
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return JsonResponse({'status': 'deleted'}, status=204)
