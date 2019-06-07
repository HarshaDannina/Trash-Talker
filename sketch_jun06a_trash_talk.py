from boltiot import Bolt, Sms #Import Sms and Bolt class from boltiot library
import json, time

garbage_full_limit = 5 # the distance between device and  garbage in dustbin in cm

API_KEY = "Bolt Cloud API"
DEVICE_ID  = "BOLTxxxxx"

# Credentials required to send SMS
SID = 'Your Twilio SID'
AUTH_TOKEN = 'Twilio Auth Token'
FROM_NUMBER = 'No. in your Dashboard'
TO_NUMBER = 'Twilio Verified No.'

mybolt = Bolt(API_KEY, DEVICE_ID) #Create object to fetch data
sms = Sms(SID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER) #Create object to send SMS
response = mybolt.serialRead('13')
print response


while True:
    try:
        response = mybolt.serialRead('13')  #Fetching the value from Arduino
        data = json.loads(response)
        #print data
        garbage_value = data['value'].rstrip()
        print "Garbage level is", garbage_value
        #print type(garbage_value)
        if int(garbage_value) < garbage_full_limit:
            response = sms.send_sms('Hello Harsha, I am full- Trash Talker')
        time.sleep(30)

    except KeyboardInterrupt:
        break
