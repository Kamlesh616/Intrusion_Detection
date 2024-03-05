from twilio.rest import Client
account_sid = 'account_id'
auth_token = 'auth_token'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='+16203038645',
    body='Alert ',
    to='+919021356110'
    )

    print(message.sid)