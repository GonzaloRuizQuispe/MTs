import pyotp

secret = 'OAHTLYV7LQEPUIMTM2UCQNX7FDGZKQMG'

print("Mi Secreto:", secret)

totp_object = pyotp.TOTP(secret)

qr_text = totp_object.provisioning_uri(name="Administrador", issuer_name="MTs")

print(qr_text)

otp = input("Ingresa El OTP: ")

if totp_object.verify(otp):
    print("Verificado")
else:
    print("No Verificado")