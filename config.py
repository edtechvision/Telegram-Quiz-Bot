
import ngrok


QUIZ_BOT_NAME = "Target Board official Bot"
NGROK_TOKEN = "2qteLYgvgJx8WDAUflzGuV3ds55_7QcJBvKmDGWiDBSWN9uKU"
API_KEY = "7786340454:AAE0-KY5FkpVj9TRHD7YzxhnTQ21AGdYov0"

_update_ = {
    "update":"webhook integration-1",
    "description":"webhook integration was done for scaling the bot for large number of users.[30/01/2024]"
}

listener = ngrok.forward("localhost:8443", authtoken=NGROK_TOKEN)


URL = listener.url()


