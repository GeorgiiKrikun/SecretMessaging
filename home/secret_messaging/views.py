from django.shortcuts import render

def create_secret(request):
    return render(request, 'secret_messaging/create_secret_string.html')
    
def reveal_secret(request):
    return render(request, 'secret_messaging/reveal_secret_string.html')

