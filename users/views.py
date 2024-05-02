from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from users.models import Payments
from users.serializers import PaymentSerializer
from users.services import create_stripe_product, create_stripe_price, create_stripe_session


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payment_course', 'method']
    ordering_fields = ['payment_date']

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        print(payment)
        stripe_prod_id = create_stripe_product(payment)
        stripe_price_id = create_stripe_price(payment, stripe_prod_id)
        payment.session_id, payment.payment_link = create_stripe_session(stripe_price_id)
        payment.save()
