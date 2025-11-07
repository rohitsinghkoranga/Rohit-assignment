from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Count
import os
import redis
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework import status
from drf_spectacular.utils import extend_schema

def get_redis_client():
    return redis.Redis(
        host=os.getenv("REDIS_HOST", "localhost"),
        port=int(os.getenv("REDIS_PORT", 6379)),
        db=int(os.getenv("REDIS_DB", 0)),
        decode_responses=True
    )

@api_view(["GET"])
def stats_view(request):
    r = get_redis_client()
    total_requests = r.get("api_request_count") or 0
    total_transactions = Transaction.objects.count()
    print(f"[stats_view] Total requests: {total_requests}, Total transactions: {total_transactions}")
    return Response({
        "total_requests": int(total_requests),
        "total_transactions": total_transactions,
    }, status=status.HTTP_200_OK)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by("-transaction_time")
    serializer_class = TransactionSerializer

    @extend_schema(description="List transactions with optional filters")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django is working perfectly!")