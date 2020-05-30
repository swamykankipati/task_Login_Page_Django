from django import forms
from portal.models import Register

class registrationform(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['firstName','emailId']

    