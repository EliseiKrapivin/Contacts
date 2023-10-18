from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('second_name','name', 'surname','phone_number','email','birthday')