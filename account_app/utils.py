from zeep import Client, Settings
#client class in zeep used to connect and interact with soap web services
from zeep.transports import Transport
#transport class in zeep manages network connection to the soap server and http headers and sessions
from requests import Session
#session allows python to make http requests

#create a soap client (zeep) to communicate with soap requests
def soap_client():
    session = Session()
    session.headers.update({
        'Content-Type': 'application/soap+xml',  
        #this header tells the soap service that the request data is in xml format
    })

    transport = Transport(session=session)
    #create a client object to interact with our soap service 
    client = Client('http://localhost:8000/bank/soap/?wsdl', transport=transport)
    print("Session headers:", session.headers)
    return client
