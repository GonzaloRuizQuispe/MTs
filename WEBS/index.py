from re import S, X
from flask import Flask, render_template, request, redirect, url_for, session
import pyotp
from pyotp import totp

#Librerias Propias
secret = pyotp.random_base32()
print("Mi Secreto:", secret)
totp_object = pyotp.TOTP(secret)
qr_text = totp_object.provisioning_uri(name="Administrador", issuer_name="MTs")
print(qr_text)
#----------------

app = Flask(__name__)

@app.route('/Home')
def Home():

    return render_template('Hofice.html')


@app.route('/MiCuenta')
def MiCuenta():
    return render_template('MiCuenta.html')


@app.route('/Info')
def info():
    return render_template('Info.html')


@app.route('/Login', methods = ["GET","POST"])
def Login():
    if request.method == 'POST':

        code = request.form['password']
        totp_object = pyotp.TOTP(secret)
        valid = totp_object.verify(code)
        print(code)
        if valid == 'true':
            return render_template('Hofice.html')
        else:
            return render_template('Login.html')
    else:
        return render_template('Login.html')


if __name__ == '__main__':
    app.run(debug=True)
