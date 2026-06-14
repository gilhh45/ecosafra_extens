from django.db import models

class Client(models.Model):
    
    nome = models.CharField(max_length=255)
    
    cpf_cnpj = models.CharField(max_length=20, unique=True) 
    
    propriedade = models.CharField(max_length=255, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    servico_principal = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default='Ativo')

    def __str__(self):
        return f"{self.nome} - {self.propriedade}"
