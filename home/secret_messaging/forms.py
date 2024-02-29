from django import forms

class create_secret_form(forms.Form):
    message = forms.CharField(label='message', max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}))
    secret = forms.CharField(label='secret', max_length=200, widget=forms.TextInput(attrs={'class': 'form-input'}))

class reveal_secret_form(forms.Form):
    secret_string = forms.CharField(label='secret string')