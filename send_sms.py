
# Jesse Coull April 6 2015
# Zagster project

from twilio.rest import TwilioRestClient

# Account Sid and Auth Token from twilio.com/user/account
# Executed with trial account authorization level

account_sid = "{insert 34 digit account sid}"

auth_token = "{insert authorization token}"

client = TwilioRestClient(account_sid, auth_token)

# Construct message body and outgoing/receiving number

message = client.messages.create(body="Hello world!",
                                 to="+{receiving number}",
                                 from_= "+{outgoing number}")


#Print message sid in terminal

print message.sid 
