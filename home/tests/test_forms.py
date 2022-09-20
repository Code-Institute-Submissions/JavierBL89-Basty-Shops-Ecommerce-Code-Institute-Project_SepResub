from django.test import TestCase

from checkout.forms import OrderForm


class TestOrderForm(TestCase):
    """
    Class to test OrderForm
    """
    def test_item_name_is_required(self):
        """
        Test full name field is required
        """
        form = OrderForm({'full_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(form.errors['full_name'][0],
                         'This field is required.')

    def test_item_phone_number_is_required(self):
        """
        Test phone number field is required
        """
        form = OrderForm({'phone_number': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(form.errors['phone_number'][0],
                         'This field is required.')

    def test_item_email_is_required(self):
        """
        Test phone number field is required
        """
        form = OrderForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0],
                         'This field is required.')

    def test_fields_are_explicit_in_forms_metaclass(self):
        """
        Test fields are explicit in forms metaclass
        """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ['full_name',
                                            'email',
                                            'phone_number',
                                            'street_address_1',
                                            'street_address_2',
                                            'town_or_city',
                                            'post_code',
                                            'country',
                                            'county'])
