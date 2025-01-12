import smtplib
smptObj = smtplib.SMTP('smtp.gmail.com',587)
a = smptObj.ehlo()
print(a)
b = smptObj.starttls()
print(b)

email = input("Please Enter your mail Id: ")
password = input('Enter 2-step Google Apps Password:  ')
smptObj.login(email,password)
from_add = email
to_add = input("Please enter Reciver Mail Id: ")
subjct = "THIS IS PYTHON GENERATED MAIL FROM"+email
Msg = input("Enter you Messege: ")
messege = "Subject:"+subjct+'\n'+Msg
smptObj.sendmail(from_add,to_add,messege)
smptObj.quit()

