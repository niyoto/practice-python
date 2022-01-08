from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)

call = client.messages.create(
    to="447376176541",
    from_="447830378021",
    body="From Niyi (your concubine) - planning anything for dinner other than  rice"
)


