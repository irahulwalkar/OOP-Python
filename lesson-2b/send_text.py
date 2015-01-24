from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACffb9b228518d26ecf02160940d8ee692"
auth_token  = "96f6349e46a51e07baf8762a90add172"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="My name is Rahul Walkar?",
    to="+919870891610",    # Replace with your phone number
    from_="+18589240221") # Replace with your Twilio number
print message.sid
