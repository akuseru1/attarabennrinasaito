from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tenki')
def tenki():
    return render_template('tenki.html')

@app.route('/yotei')
def yotei():
    return render_template('yotei.html')

@app.route('/resipi')
def resipi():
    return render_template('resipi.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)