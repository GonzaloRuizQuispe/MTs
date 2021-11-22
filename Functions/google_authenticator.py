import pyotp

secret = pyotp.random_base32()
print("Mi Secreto:", secret)

totp_object = pyotp.TOTP(secret)

qr_text = totp_object.provisioning_uri(name="Administrador", issuer_name="MTs")

print(qr_text)

otp = input("Ingresa El OTP: ")
valid = totp_object.verify(otp)
print(valid)