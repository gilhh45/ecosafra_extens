from django.shortcuts import render
from .models import Client 

def client_list(request):
    
    all_clients = Client.objects.all() 
    
    return render(request, 'templates/index.html', {'clients': all_clients})


