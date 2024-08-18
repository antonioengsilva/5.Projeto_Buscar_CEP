# myapp/views.py

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import requests

class ConsulteCEPView(generics.ListCreateAPIView):
    def get(self, request):
        cep = request.GET.get('cep', '')
        if not cep:
            return render(request, 'consulta_cep.html', {'error': 'Digite um CEP.'})

        url = f'https://viacep.com.br/ws/{cep}/json/'
        response = requests.get(url)

        if response.status_code != 200 or 'erro' in response.json():
            return render(request, 'consulta_cep.html', {'error': 'Erro ao buscar o CEP.'})

        data = response.json()
        return render(request, 'consulta_cep.html', {
            'cep': cep,
            'logradouro': data.get('logradouro'),
            'bairro': data.get('bairro'),
            'cidade': data.get('localidade'),
            'estado': data.get('uf'),
        })

    def post(self, request):
        return self.get(request)
