from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from users.models import Payments
from users.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payment_course', 'method']
    ordering_fields = ['payment_date']
