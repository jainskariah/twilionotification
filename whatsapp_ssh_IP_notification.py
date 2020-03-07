from twilio.rest import Client
import subprocess
import re
account_sid = 'ACCOUNT_SID'
auth_token = 'AUTH_TOKEN_TWILIO'
client = Client(account_sid, auth_token)
address = open("/var/log/secure", "r")
for line in address:
    if re.match("(.*)Accepted(.*)", line):
        file = open("/tmp/sample.txt","w")
        file.write(line)
file.close()
lastline=open("/tmp/sample.txt", "r")
for finalline in lastline:
    finalline=finalline.split()
    message = client.messages.create(
                              from_='whatsapp:+1234567890',
                              body="SSH login alert from IP:"+finalline[10],
                              to='whatsapp:+0987654321'
                          )
print(message.sid)
