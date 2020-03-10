# twilionotification

This code is used to send Notification to Whatsapp Number using twilion application.

This script is setup to send a notification message to Whatsapp Numeber when some one login to Server by SSH. This is setup using who command result as a result all the active user section IP list will be send as notification.

Ensure to add the code on the .Bashrc file so that the code will get executed.

python2 whatsapp.py


#whatsapp_ssh_IP_notification.py

This code that will only list the SSH login section users IP address.

#usinglastcommand.py

This Script will fetch the details of login IP using LAST command in Linux and notify the Client.
This will be the best choice to use as compared to other two script this will not take much time and execution is much faster.

Script whatsapp.py and whatsapp_ssh_IP_notification.py this by use secure log to fetch details. If the log size is in GB then the time taken to read and send the details is much higher compared to using Last Command function.
