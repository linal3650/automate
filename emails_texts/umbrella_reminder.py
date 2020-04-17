#! python3
# umbrella-reminder.py - Checks the weather forecast and text an umbrella reminder if it's raining

import requests, bs4
from twilio.rest import Client

def rain_check():
    # Check weather.gov to see if it is likely to rain today
    url = 'https://weather.com/en-GB/weather/today/l/<your location>'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    weatherElem = soup.select('#dp0-phrase')
    weather = weatherElem[0].getText()

    if 'rain' in weather.lower():
        return True

accountSID = '<twilio ID>'
authToken = '<twilio token>'
twilioNumber = '<twilio number>'
myNumber = '<your mobile number>'

def text_myself(message):
    # Use Twilio to text the message argument to your phone
    twilio_cli = Client(accountSID, authToken)
    twilio_cli.messages.create(body=message, from_=twilioNumber, to=myNumber)

if rain_check():
    text_myself('Remember to bring an umbrella')
