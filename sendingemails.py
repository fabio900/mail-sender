

# import smtplib
# sender= 'ababiofrancis73@gmail.com'
# receiver =['pkblankson@yahoo.com']
# message = """From:From Person <ababiofrancis73@gmail.com>
# To: To person <pkblanson@yahoo.com>
# Subject: SMTP e-mail test
 
#  This is a test e-mail message.
#  """
# smtpObj = smtplib.SMTP('stmp.gmail.com',587)
# smtpObj.ehlo()
# smtpObj.starttls()
# smtpObj.login("ababiofrancis73@gmail.com","twitter.,")
# message="hello world"

# smtpObj.sendmail("ababiofrancis73@gmail.com","pkblankson@yahoo.com",message)
# smtpObj.quit()


# print "Successfully sent email"
# print "Error: unable to send email"

import smtplib
sender = "ababiofrancis73@gmail.com"
receiver =["pkblanks2013@gmail.com"]
message = """from: from person <ababiofrancis73@gmail.com>
To: To person <pkblanks2013@gmail.com>
Subject: SMTP email test

This is a test email message.
"""
smtpObj = smtplib.SMTP("smtp.gmail.com",587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login("ababiofrancis73@gmail.com","twitter.,")
message= "hello world"

smtpObj.sendmail("ababiofrancis73@gmail.com","pkblanks2013@gmail.com",message)
smtpObj.quit()


