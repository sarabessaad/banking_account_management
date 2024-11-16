from django.shortcuts import render
from account_app.utils import soap_client


def account_detail_view(request):
    client_email = request.GET.get('email', '')  
    account = None 

    if client_email:
        soap = soap_client()
        try:
            #we use the get_account_details that we implemented in views.py
            account = soap.service.get_account_details(client_email)
        except Exception as e:
            print("SOAP Error:", e)

    return render(request, 'account_app/account_details.html', {'account': account, 'email': client_email})