from rest_framework import serializers

from users.models import Payments, User


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('id', 'user', 'payment_date', 'payment_course', 'amount', 'method')


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'payments')
