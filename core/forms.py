from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from .models import Profile

PAYMENT_CHOICES = (
    ('S', 'Credit'),
    ('P', 'Debit')
)

from django import forms

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='Used for Login.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Your First Name.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Your Last Name.')
    email = forms.EmailField(max_length=254, help_text='Required. Please input a valid email address.')
    # Account = forms.CharField(max_length=30, required=False, help_text='Your Account Type.')
    # CHOICES=[('Personal','Personal'),
    #         ('Business','Business')]

    # Account_Type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    def clean(self):
       email = self.cleaned_data.get('email')
       username = self.cleaned_data.get('username')
       if User.objects.filter(email=email).exists() and User.objects.filter(username=username).exists() :
            raise ValidationError("Email and Username exists. Please try with different username and Email")
       elif User.objects.filter(username=username).exists():
            raise ValidationError("Useraname already exists. Please try with diifferent username")
       elif User.objects.filter(email=email).exists():
            raise ValidationError("Email exists. Please try with different email")
       return self.cleaned_data
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ProfileForm(forms.ModelForm):
    # username = forms.CharField(max_length=30, required=False, help_text='Used for Login.')
    class Meta:
        model = Profile
        fields = ['account_type']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
