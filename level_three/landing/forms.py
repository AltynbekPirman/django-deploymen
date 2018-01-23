from django import forms
from django.core import validators


def check_z(value):
    if value[0].lower() != "z":
        raise forms.ValidationError("not z")

class registerForm(forms.Form):
    name = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256)
    email_bacck = forms.EmailField(label="enter again")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super(registerForm, self).clean()
        email_first = all_clean_data['email']
        email_chek = all_clean_data['email_bacck']
        if email_first != email_chek:
            raise forms.ValidationError("mails do not match")
