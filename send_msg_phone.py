from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC90902012c16c2c804e59a0155d1c79d5"
# Your Auth Token from twilio.com/console
auth_token  = "0740a3742b91522777cc031ad83364fd"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917353091577", 
    from_="+12564740680",
    body="Hello from Python!")

print(message.sid)
