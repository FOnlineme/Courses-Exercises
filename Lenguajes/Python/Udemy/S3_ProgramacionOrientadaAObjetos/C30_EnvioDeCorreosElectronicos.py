import smtplib

remitente='julianmarceloluque@gmail.com'
destinatario='caroluque2000@gmail.com'
msg='Prueba de envio de correo con Python'

#Datos
username='julianmarceloluque@gmail.com'
password='noclanse17'

#Envio del correo
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(remitente, destinatario,msg)
server.quit()

