import smtplib

fromaddr = 'IRS'

toaddr = '18764551747@Digitextjm.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""
fromname = "maffy"

toname = "ODane",

toaddr = "18764551747@Digitextjm.com"

subject = "testing"

msg = "this works"

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