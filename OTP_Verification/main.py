import random
import smtplib

#importing email and password from the custom module credentials.py
from credentials import email, password

#creating a 6 digit otp and storing it into a varible
otp = ''.join([str(random.randint(1,9)) for i in range(6)]) #converted the list into a joined string with no spaces

#asking the user to enter their email address
receiver = input("Please enter your email address: ")

#initialising the SMTP server with Gmail's SMTP server address and port 587
server = smtplib.SMTP('smtp.gmail.com', 587)

#encrypting the contents of the server for security
server.starttls()

#logging in to the sender's email address
server.login(email,password)

#Composing email body and subject
subject = "Your OTP. Do not share this anyone!"
txt = f'Subject: {subject}\n\nThe requested otp is '  + otp

#sending the email to he user's email
server.sendmail(email, receiver, txt)

#closing the SMTP server connection
server.quit()

# Indicating that the email has been sent to the provided email address
print("email sent to: " + receiver)

#taking the OTP input from the user
num = int(input('Enter the OTP Sent at ' + receiver + ': '))

if num == int(otp):
    print("OTP verified successfully!")
else:
    print("Wrong OTP entered! Resend OTP and try again.")