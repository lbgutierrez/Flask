from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<nombre>')
def hello_name( nombre ):
	return render_template( 'hello.html', name=nombre )