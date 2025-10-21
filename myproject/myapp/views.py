from django.shortcuts import render
from myapp.braintree_config import get_client_token
from django.conf import settings

def index(request):
    
    client_token = get_client_token() 
    context = {
        'page_title': 'Welcome to My Django App',
        'content': '',
        'client_token': client_token
    }
    return render(request, 'index.html', context)
def home_page(request):
    context = {
        'page_title': 'Home Page',
        'content': 'This is another page in your app.'
    }
    return render(request, 'home_page.html', context)
