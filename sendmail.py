import smtplib

fromaddr = 'odanejackson12@gmail.com'

toaddr = '4551747@digiceljm.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""
fromname="ODane"
toname="Jackson"
toaddr="odanejackson12@gmail.com"
subject="testing"
msg="This is a test of the mail function in python"
messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddr,

 subject,

 msg)

# Credentials (if needed)

username = 'odanejackson12@gmail.com'

password = 'feorugimxdeaplob'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddr, messagetosend)

server.quit()
