from django import forms
from portfolio.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Name', 'Email','Subject' ,'Message']