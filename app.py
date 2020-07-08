from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return '<h1>Vasanthan Deployment from Git Check 123</h1>'

if __name__ == '__main__':
	app.run(debug=True)