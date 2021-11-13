from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('MTs.html')


@app.route('/about')
def about():
    return render_template('MiCuenta.html')


@app.route('/about')
def about():
    return render_template('Info.html')


if __name__ == '__main__':
    app.run(debug=True)
