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
        
        api_url = f'http://10.240.50.181:30009/api/etp/{etp}'
            
        response = requests.get(api_url)
           
        if response.status_code == 200:
            data = response.json()
            print(response)
            
            list_oes_total = lista_oes(data)
            

            context = {
                    'data': data,
                    'list_oes_total' : list_oes_total
                }
            print('entrei nas oes')
            print(list_oes_total)
            return render(request, 'usuarios/search_results.html', context)
        else:
            erro_menssagem = f"Erro {response.status_code}"
            return render(request, 'usuarios/error.html', {'erro_menssagem': erro_menssagem})
    return render(request, 'usuarios/search_results.html')
        

def error(request):
    return render(request, 'usuarios/error.html')

def lista_oes(data):

    list_elemento = data["data_smtx_oe_elemento"]
    list_circuito = data["data_smtx_oe_circuito"]
    list_odu = data["data_smtx_oe_odu"]
    list_och = data["data_smtx_oe_och"]

    list_oes_total = list_elemento + list_circuito + list_odu + list_och

    return list_oes_total
