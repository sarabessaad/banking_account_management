from spyne import ComplexModel, Decimal, Integer, Unicode, Double, Date

class Client (ComplexModel):
    cin = Integer
    name = Unicode
    familyName = Unicode
    email = Unicode

class Account (ComplexModel):
    rib = Unicode
    client = Client
    balance = Double
    AccountType = Unicode
    creationDate = Date

class Transaction (ComplexModel):
    id = Integer
    TransactionType = Unicode
    account = Account
    transactionDate = Date
    amount = Double
    description = Unicode
    transfer_to_account = Unicode