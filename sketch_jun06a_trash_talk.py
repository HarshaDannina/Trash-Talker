from boltiot import Bolt, Sms #Import Sms and Bolt class from boltiot library
import json, time

garbage_full_limit = 5 # the distance between device and  garbage in dustbin in cm

API_KEY = "2ce4c9c7-fdbe-4426-abcc-7bd94cf36fb5"
DEVICE_ID  = "BOLT3880173"

# Credentials required to send SMS
SID = 'AC47aec30690ee078250eba59f25630893'
AUTH_TOKEN = '9ea707e96f75d6094557b1c9186033c0'
FROM_NUMBER = '+16084716734'
TO_NUMBER = '+917095675760'

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
