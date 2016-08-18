import urllib2
import json
from twilio.rest import TwilioRestClient

#twilio client
client = TwilioRestClient(account='ACf71fb04945327b0773ffae89a51d651d',
token="5b0729d9252c69572996c8b5db35655f")

#phone numbers
my_number  = '+441173255426'
her_number = '+447526512854'

#api for ISS location
req = urllib2.Request("http://api.open-notify.org/iss-now.json")
response = urllib2.urlopen(req)
obj1 = json.loads(response.read())

#api for number of astros in space
req = urllib2.Request("http://api.open-notify.org/astros.json")
response = urllib2.urlopen(req)
obj2 = json.loads(response.read())

number = (int(obj2['number']))


#returned values
timestamp = ('Timestamp: ' + str(obj1['timestamp']))
latitude = (str(obj1['iss_position']['latitude']))
longitude = (str(obj1['iss_position']['longitude']))

locationtext = ('Lat: ' + latitude + 'Long: ' + longitude)

print
print (timestamp)
print (locationtext)
print
print('Number of people in space: ' + str(number))



#send text message
'''
client.messages.create(
    to=her_number,
    from_=my_number,
    body= locationtext)
'''

print("Message sent!")
