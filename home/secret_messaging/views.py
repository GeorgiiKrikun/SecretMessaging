from django.shortcuts import render, redirect

def redirect_view(request):
    response = redirect('secret_string')
    return response

def create_secret(request):
    return render(request, 'secret_messaging/create_secret_string.html')
    
def reveal_secret(request):
    return render(request, 'secret_messaging/reveal_secret_string.html')

