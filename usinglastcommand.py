from twilio.rest import Client
import subprocess
import re
account_sid = 'ACCOUNT_TWILION'
auth_token = 'AUTH_TWILION'
client = Client(account_sid, auth_token)
import os, subprocess
out = subprocess.Popen('last', 
           stdout=subprocess.PIPE,)
subprocess.call(['last'], stdout=subprocess.PIPE, shell=True)
sort = subprocess.Popen(['head', '-1'], stdin=out.stdout, stdout=subprocess.PIPE,)
end_of_pipe = sort.stdout
for ip in end_of_pipe:
  login = ip.split()[2]
#  print(login)
  message = client.messages.create(
                              from_='whatsapp:+123456789',
                              body="SSH login alert from IP:"+login,
                              to='whatsapp:+1234567890'
                          )
print(message.sid)
