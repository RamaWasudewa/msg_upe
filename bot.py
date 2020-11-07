from twilio.rest import Client 
 
account_sid = 'AC912ee14df0e55c530e3abed534cc05bf' 
auth_token = 'c532d872789201286873469768eeb20c' 
client = Client(account_sid, auth_token) 
def send_msg():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello Boy',      
                              to='whatsapp:+628563893800' 
                          ) 
 
    print(message.sid)
