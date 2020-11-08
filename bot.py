from twilio.rest import Client 
 
account_sid = 'AC912ee14df0e55c530e3abed534cc05bf' 
auth_token = '386ad879c0f58871183916a5a80ee4f7' 
client = Client(account_sid, auth_token) 
def send_msg():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hi Upe Bodo!!!',      
                              to='whatsapp:+628563893800' 
                          ) 
 
    print(message.sid)
