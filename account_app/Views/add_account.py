from django.shortcuts import render, redirect
from django.contrib import messages
from account_app.utils import soap_client
from account_app.forms import AccountForm
from account_app.complexTypes import Account as complexAccount, Client as complexClient


def add_account_view(request):
    if request.method == 'POST':
        print("form submission received")
        form = AccountForm(request.POST)
        if form.is_valid():
            #form.cleaned_data va creer un dictionnaire with the data from the form
            data = form.cleaned_data
            soap = soap_client()

            account_data = {
                "rib": data['rib'],
                "balance": float(data['balance']),
                "client": {  
                    "cin": data['client_cin'],
                    "name": data['client_name'],
                    "familyName": data['client_family_name'],
                    "email": data['client_email']
                },
                "creationDate": data['creation_date']
            }

            try:
                # call SOAP API to add account (the add_account we implemented in views.py)
                response = soap.service.add_account(account_data)
                return redirect('home')
            except Exception as e:
                print("SOAP Error:", e)
                messages.error(request, "An error occurred while adding the account.")
        else : 
            print("Form is not valid")  
            print(form.errors)  
    else:
        form = AccountForm()
    return render(request, 'account_app/add_account.html', {'form': form})
