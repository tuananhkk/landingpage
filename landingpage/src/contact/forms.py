from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name",
            "email",
            "phone",
            "content"
        ]
        
# class ContactForm(forms.Form):
#     name = forms.CharField(max_length = 255, required=True)
#     email = forms.EmailField(required=True)
#     phone = PhoneNumberField()
#     content = forms.CharField(widget=forms.Textarea, max_length = 150)



