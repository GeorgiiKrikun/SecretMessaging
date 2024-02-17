from django.http import HttpResponse
from django.shortcuts import render
from .forms import create_secret_form, reveal_secret_form  # Import your custom form
from .InvisibleSymbolBinary import make_string_invisible, make_string_visible, extract_important_symbols

def create_secret(request):
    if request.method == 'GET':
        form = create_secret_form()  # Create an instance of your form
        return render(request, 'secret_messaging/create_secret_string.html', {'form': form})
    if request.method == 'POST':
        form = create_secret_form(request.POST)
        message = form.data['message']
        secret = form.data['secret']
        secret_string = make_string_invisible(secret)
        result = message + secret_string
        return render(request, 'secret_messaging/results_secret.html', {'secret_string': result})
    
def reveal_secret(request):
    if request.method == 'GET':
        form = reveal_secret_form()  # Create an instance of your form
        return render(request, 'secret_messaging/reveal_secret.html', {'form': form})
    if request.method == 'POST':
        form = reveal_secret_form(request.POST)
        secret_string = form.data['secret_string']
        secret = extract_important_symbols(secret_string)
        result = make_string_visible(secret)
        return render(request, 'secret_messaging/results_reveal.html', {'secret_string': result})
        
def index(request):
    return render(request, 'secret_messaging/index.html')

