from twilio.rest import Client
import config


client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to="7852261305",
    from_="8397772251",
    body="This is our first message"
)

print(call.date_sent)
