import stripe
from config.settings import STRIPE_API_KEY

api_key = STRIPE_API_KEY


def create_stripe_product(course):
    course = course.payment_course
    stripe.api_key = api_key
    stripe_product = stripe.Product.create(name=course)
    return stripe_product.get("id")


def create_stripe_price(amount, product_id):
    stripe.api_key = api_key
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount.amount * 100,
        product=product_id,
    )


def create_stripe_session(price):
    stripe.api_key = api_key
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
