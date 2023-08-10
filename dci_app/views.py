from django.shortcuts import render

from django.shortcuts import render
import requests
import pdb


def home(request):
    return render(request, 'usuarios/home.html')


def search_results(request):
    print(request.body)
    print('Entrei na função')
    if request.method =='GET':
        etp = request.GET.get('search_results')
        print(etp)
        
        api_url = f'http://10.240.50.180:30009/api/etp/{etp}'
            
        response = requests.get(api_url)
           
        if response.status_code == 200:
            data = response.json()
            print(response)

            dicionario = data

            list_elemento = [dicionario["data_smtx_oe_elemento"]]
            list_circuito = [dicionario["data_smtx_oe_circuito"]]
            list_odu = [dicionario["data_smtx_oe_odu"]]
            list_os_total = list_elemento + list_circuito + list_odu
            print(list_os_total)
            
            context = {
                    'data': data
                }

            return render(request, 'usuarios/search_results.html', context)
        else:
            erro_menssagem = f"Erro {response.status_code}"
            return render(request, 'usuarios/error.html', {'erro_menssagem': erro_menssagem})
    return render(request, 'usuarios/search_results.html')
        

def error(request):
    return render(request, 'usuarios/error.html')

def lista_oes():

    dicionario = search_results()

    list_elemento = [dicionario["data_smtx_oe_elemento"]]
    list_circuito = [dicionario["data_smtx_oe_circuito"]]
    list_odu = [dicionario["data_smtx_oe_odu"]]

    list_os_total = list_elemento + list_circuito + list_odu

    return(list_os_total)

