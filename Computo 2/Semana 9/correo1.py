import smtplib

remit = "zapatad308@gmail.com"
serv = "smtp.gmail.com"
puerto = 587
contra = "nczd dvxa njjw plzd"
try:
    conex = smtplib.SMTP(serv,puerto)
    conex.starttls()
    conex.login(remit,contra)
    conex.sendmail(remit,remit,"Subject: Probando correo "
                      "\n\n Este correo es automatico")
    print("El correo se ha mandado correctamente")
except smtplib.SMTPException as e:
    print(f"Error al mandar el mensaje: {e}")
finally:
    conex.quit()