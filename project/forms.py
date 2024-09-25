from django import forms
from .validators import validate_no_special_characters,validate_phone_number

class UserInfoForm(forms.Form):
    name = forms.CharField(max_length=100,validators=[validate_no_special_characters])
    surname = forms.CharField(max_length=100,validators=[validate_no_special_characters])
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField()
    phone = forms.CharField(max_length=10,validators=[validate_phone_number])
