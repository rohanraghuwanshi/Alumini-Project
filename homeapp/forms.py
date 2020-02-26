from django import forms

from .models import ContactRequest

#Forms creation

class ContactRequestForm(forms.ModelForm):
    
    class Meta:
        model = ContactRequest
        fields = (
                "name",
                "email",
                "phone",
                "text"
            )

        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'placeholder':'Name'
                }
            ),
            'email' : forms.EmailInput(
                attrs={
                    'placeholder':'Email'
                }
            ),
            'phone' : forms.TextInput(
                attrs={
                    'placeholder':'Phone number'
                }
            ),
            'text' : forms.Textarea(
                attrs={
                    'placeholder':'Write your query here...',
                    'rows':'5'
                }
            )
        }
