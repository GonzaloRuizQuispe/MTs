from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
