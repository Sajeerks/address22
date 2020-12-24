from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = ['names', 'email', 'phone', 'city', 'state', 'zipcode']