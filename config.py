
import ngrok


QUIZ_BOT_NAME = "SAMPLE BOT NAME"
NGROK_TOKEN = "YOUR NGROK AUTH TOKEN"
API_KEY = "YOUR TELEGRAM QUIZ BOT API KEY"

_update_ = {
    "update":"webhook integration-1",
    "description":"webhook integration was done for scaling the bot for large number of users.[30/01/2024]"
}

listener = ngrok.forward("localhost:8443", authtoken=NGROK_TOKEN)


URL = listener.url()


