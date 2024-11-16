from suds.client import client

url='http://127.0.0.1:8000/account/?wsdl'
client=Client(url)

account_data=client.factory.create('Account')
account_data.account_name='Sara'
account_daat.balance=1000
response=client.service.create_account(account_data)
print(response)

transaction_data=client.factory.create('Transaction')
transaction_data.account_name='Sara'
transaction_data.amount=350
transaction_data.transaction_type='deposit'
response=client.service.deposit(transaction_data)
print(response)



