from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from users.models import Payment
from users.serliazers import PaymentSerializer


# Create your views here.

class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = {
        "paid_course": ["exact"],
        "paid_lesson": ["exact"],
        "payment_method": ["exact"],
    }
    ordering_fields = ["payment_date"]
    ordering = ["payment_date"]
