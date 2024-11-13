from django.shortcuts import render
from zeep import Client


def add_account_view(request):
    #? Verification de la methode de soumission de données 
    if request.method == 'POST':
        #? Recuperation des données a partir du formulaire 
        account_data = {
            'rib': request.POST['rib'],
            'client': {
                'cin': request.POST['cin'],
                'name': request.POST['name'],
                'familyName': request.POST['familyName'],
                'email': request.POST['email']
            },
            'balance': request.POST['balance'],
            'creationDate': request.POST['creation_date']
        }

        #? appl du service soap 
        client = Client('http://localhost:8000/bank/?wsdl') 
        try:
            result = client.service.add_account(account_data)
            return render(request, 'add_account.html', {'message': result})
        except Exception as e:
            return render(request, 'add_account.html', {'error': str(e)})
    
    return render(request, 'add_account.html')

def account_details_view(request):
    if request.method == 'POST':
        email = request.POST['email']

        #? Appel du service soap 
        client = Client('http://localhost:8000/bank/?wsdl')  
        try:
            account = client.service.get_account_details(email)
            return render(request, 'account_details.html', {'account': account})
        except Exception as e:
            return render(request, 'account_details.html', {'error': str(e)})

    return render(request, 'account_details.html')

def all_accounts_view(request):
    client = Client('http://localhost:8000/bank/?wsdl') 
    try:
        #? Recuperation de tout les clients 
        accounts = client.service.get_all_accounts()
        return render(request, 'all_accounts.html', {'accounts': accounts})
    except Exception as e:
        return render(request, 'all_accounts.html', {'error': str(e)})


