from .views import bank_soap_app
from django.urls import path
from .Views.home import home_view
from .Views.account_details import account_detail_view
from .Views.add_account import add_account_view

urlpatterns = [
    path("soap/", bank_soap_app),
    path("home/", home_view, name='home'),
    path("account/details", account_detail_view, name="account_details"),
    path("add-account/", add_account_view, name="add_account"),
]