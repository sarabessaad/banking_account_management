from django.shortcuts import render
from spyne.service import ServiceBase
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Double
from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from spyne import ComplexModel, Decimal
from .models import Account as modelAccount,Transaction as modelTransaction, Client as modelClient
from .complexTypes import Account as complexAccount, Client as complexClient, Transaction as complexTransaction

# Create your views here.

class AccountService(ServiceBase):
    @rpc(complexAccount, _returns=Unicode)
    def add_account(self, account):
        if account.client is None:
            return "Error: Client information is missing in the account data."

        acc_exists = modelAccount.objects.filter(rib=account.rib).exists()
        if acc_exists:
            print("Account already exists:", account.rib)
            return 'This account already exists'

        #verify if the client exists
        #the way we did it in class(client=modelClient.objects.get(pk=account.client.cin)) creates a problem when the client doesn't exist 
        #so instead get_or_create (django method that retrieves an object from the db and if it doesn't exist creates it)
        client, client_created = modelClient.objects.get_or_create(
            cin=account.client.cin,
            defaults={
                'name': account.client.name,
                'familyName': account.client.familyName,
                'email': account.client.email,
            }
        )
        print("Client found or created:", client, "Created:", client_created)
        #convert from account complex type into model account
        acc = modelAccount(
            rib=account.rib,
            balance=account.balance,
            client=client,
            creation_date=account.creationDate
        )
        acc.save()
        print("Account created with RIB:", acc.rib)
        return f'The account with RIB {account.rib} has been successfully created.'
        
    @rpc(Unicode, _returns=complexAccount)
    def get_account_details(self, email):
        try:
            account = modelAccount.objects.filter(client__email__iexact=email).first()
            if not account:
                raise ValueError(f"No account associated with the email {email}")

            #convert the model account to a complexType account
            complexAcc = complexAccount()
            complexAcc.rib=account.rib
            complexAcc.balance=float(account.balance) 
            #we have to convert it to float because zeep onlyy knows how to handle simple types (int, float)(or else it will show as none)
            complexAcc.client=account.client
            complexAcc.creationDate=account.creation_date
            return complexAcc

        except Exception as e:
            print("SOAP Error:", e)
            raise e




#create a Spyne application (soap)
#configuration of the soap API
application=Application(
    [AccountService],
    tns='bankapp.isg.tn',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)
#create a django application
django_app=csrf_exempt(DjangoApplication(application))
bank_soap_app=csrf_exempt(django_app) #csrf = cross site request forgery 

def soap_service(request):
    return HttpResponse(soap_application(request))