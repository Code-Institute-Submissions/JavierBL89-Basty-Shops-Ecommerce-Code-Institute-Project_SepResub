from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile()
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_country': 'Country',
            'default_post_code': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address_1': 'Street Address 1',
            'default_street_address_2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black profile-form-input'
            self.fields[field].label = False


class UpdateUserForm(forms.ModelForm):

    name = forms.CharField(max_length=100,
                           required=True)
    surname = forms.CharField(max_length=100,
                              required=True)
    username = forms.CharField(max_length=100,
                               required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['name', 'surname', 'username', 'email']

