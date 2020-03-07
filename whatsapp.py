# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import subprocess
account_sid = 'SID_ACCOUNTID'
auth_token = 'AUTH_TOKEN'
client = Client(account_sid, auth_token)
value = subprocess.Popen('who', stdout=subprocess.PIPE,)
subprocess.call(['who'], stdout=subprocess.PIPE, shell=True)
cut = subprocess.Popen(['awk', '{print $5}'],
                        stdin=value.stdout,
                        stdout=subprocess.PIPE,
                        )
end_of_pipe = cut.stdout
for ip in end_of_pipe:
 message = client.messages.create(
                              from_='whatsapp:+123456789',
                              body="SSH login alert from IP:"+ip.strip(),
                              to='whatsapp:+987654321'
                          )
print(message.sid)
