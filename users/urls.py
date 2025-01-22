from django.urls import path

from users.apps import UsersConfig
from .views import PaymentList

# Описание маршрутизации для User

app_name = UsersConfig.name

urlpatterns = [
    path("payments/", PaymentList.as_view(), name="payment-list"),
]
