from django.http import HttpResponse
from django.shortcuts import render
from .forms import request_form, request_unsecret  # Import your custom form
from .InvisibleSymbolBinary import make_string_invisible, make_string_visible, extract_important_symbols

def display_form(request):
    if request.method == 'GET':
        form = request_form()  # Create an instance of your form
        return render(request, 'secret_messaging/create_secret_string.html', {'form': form})
    if request.method == 'POST':
        form = request_form(request.POST)
        message = form.data['message']
        secret = form.data['secret']
        secret_string = make_string_invisible(secret)
        result = message + secret_string
        return render(request, 'secret_messaging/results_secret.html', {'secret_string': result})
    
def reveal_secret(request):
    if request.method == 'GET':
        form = request_unsecret()  # Create an instance of your form
        return render(request, 'secret_messaging/reveal_secret.html', {'form': form})
    if request.method == 'POST':
        form = request_unsecret(request.POST)
        secret_string = form.data['secret_string']
        secret = extract_important_symbols(secret_string)
        result = make_string_visible(secret)
        return render(request, 'secret_messaging/results_reveal.html', {'secret_string': result})
        
def index(request):
    return render(request, 'secret_messaging/index.html')

