from django import forms

class AccountForm(forms.Form):
    rib = forms.CharField(label="Account RIB", max_length=30)
    balance = forms.DecimalField(label="Initial Balance", max_digits=15, decimal_places=3)
    client_cin = forms.CharField(label="Client CIN", max_length=9)
    client_name = forms.CharField(label="Client Name", max_length=255)
    client_family_name = forms.CharField(label="Client Family Name", max_length=255)
    client_email = forms.EmailField(label="Client Email")
    creation_date = forms.DateField(label="Creation Date", widget=forms.SelectDateWidget)