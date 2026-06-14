from django.shortcuts import render, redirect
from .models import Client

def client_list(request):
    all_clients = Client.objects.all()
    return render(request, 'index.html', {'clients': all_clients})

def client_create(request):
    if request.method == 'POST':
        # 1. Captura os dados enviados pelo name="" do HTML
        nome = request.POST.get('nome')
        cpf_cnpj = request.POST.get('cpf_cnpj')
        property_name = request.POST.get('property_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        main_service = request.POST.get('main_service')
        
        # 2. Salva no banco de dados usando os nomes EXATOS do seu models.py
        Client.objects.create(
            nome=nome,
            cpf_cnpj=cpf_cnpj,
            propriedade=property_name,        
            telefone=phone,                   
            email=email,
            servico_principal=main_service,   
            status='s-approved'               
        )
        
        # Recarrega a página de listagem já com o novo cliente
        return redirect('home')
        
    return redirect('home')