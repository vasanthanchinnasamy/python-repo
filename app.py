from flask import Flask

app = Flask(__name__)

@app.route('/index')
def index():
    return '<h1>Vasanthan Deployment Check</h1>'

if __name__ == '__main__':
	app.run(debug=True)