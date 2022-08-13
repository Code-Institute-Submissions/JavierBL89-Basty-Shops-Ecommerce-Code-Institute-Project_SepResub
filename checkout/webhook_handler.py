from django.http import HttpResponse
from .models import Order, OrderLineItem

from products.models import Product

import time
import json


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandler Webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment intent succeeded webhook from stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.adddress[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name_iexact=shipping_details.name,
                    email_iexact=billing_details.email,
                    phone_number_iexact=shipping_details.phone_number,
                    country_iexact=shipping_details.address.country,
                    post_code_iexact=shipping_details.address.post_code,
                    city_iexact=shipping_details.address.city,
                    street_address_1_iexact=shipping_details.address.line1,
                    street_address_2_iexact=shipping_details.address.line2,
                    county_iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} \
                 | SUCCESS: Verified order already in database',
                status=200
                )
        else:
            order = None
            try:
                order = Order.objects.create(
                        full_name=shipping_details.name,
                        email=billing_details.email,
                        phone_numbe=shipping_details.phone_number,
                        country=shipping_details.address.country,
                        post_code=shipping_details.address.post_code,
                        city=shipping_details.address.city,
                        street_address_1=shipping_details.address.line1,
                        street_address_2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        original_bag=bag,
                        stripe_pid=pid
                    )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(pk=item_id)
                    for size, quantity in item_data['item_size'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                   content=f'Webhook received: {event["type"]} | ERROR: {e}',
                   status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
