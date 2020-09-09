import smtplib

sender_email = "xyzother@gmail.com"
rec_email = "youvvk@gmail.com"
password = input(str("Please Enter your password :"))
message = "Hey, This was sent by using Python"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Success.")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
