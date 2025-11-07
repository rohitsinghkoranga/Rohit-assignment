from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, stats_view, home

router = DefaultRouter()
router.register("transactions", TransactionViewSet, basename="transaction")

urlpatterns = [
    path("", home, name="home"),          # homepage
    path("stats/", stats_view, name="stats"),  # stats API
    path("", include(router.urls)),       # transaction API routes
]