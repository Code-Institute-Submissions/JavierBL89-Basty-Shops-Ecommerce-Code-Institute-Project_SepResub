from django import forms
from .models import Subscription


class SubscriptionForm(forms.ModelForm):

    class Meta:

        model = Subscription
        fields = ('fname', 'email',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        placeholders = {
            'fname': 'First name',
            'email': 'Email address',
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
