from django import forms

class request_form(forms.Form):
    message = forms.CharField(label='message', max_length=100)
    secret = forms.CharField(label='secret', max_length=100)

class request_unsecret(forms.Form):
    secret_string = forms.CharField(label='secret_string')