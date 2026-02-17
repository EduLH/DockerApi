from django.core.management.base import BaseCommand
from django.db.models import Sum
from expenses.models import Expense
from datetime import datetime
import requests
import os

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        month = datetime.now().month

        expenses = Expense.objects.filter(
            created_at__month=month
        )

        summary = expenses.values("category") \
            .annotate(total=Sum("amount"))

        report = "📊 Relatório Mensal\n\n"

        total_general = 0

        for item in summary:
            report += f"{item['category']}: R$ {item['total']}\n"
            total_general += item["total"]

        report += f"\nTotal: R$ {total_general}"
        print(report)
        # Aqui envia via WhatsApp Cloud API
        # requests.post(...)
