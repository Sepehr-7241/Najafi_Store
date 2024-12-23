from django import forms
from .models import ContactUs
from django_ckeditor_5.fields import CKEditor5Widget


class ContactUsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["message"].required = True

    message = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        fields = ['full_name', 'email', 'title', 'message']
        model = ContactUs
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control font'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control font'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control font'
            }),
        }
