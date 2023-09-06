from flask import Flask, render_template

app = Flask('__name__')

@app.route('/')
def home():
    return 'Hello world!!'

app.run(debug=True)