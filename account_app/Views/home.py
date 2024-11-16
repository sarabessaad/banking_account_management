
from django.shortcuts import render
#render is used to kind of work on an HTML template (adding data) and return it as an HTTP response
from account_app.utils import soap_client
from account_app.models import Account


def home_view(request):
    client_email = request.GET.get('email', '')

    if client_email:
        #redirect the user to the account details page with the email address as a parameter
        return redirect(f"{reverse('account_details')}?email={client_email}")

    #return the home.html if no email is provided 
    return render(request, 'account_app/home.html')

    