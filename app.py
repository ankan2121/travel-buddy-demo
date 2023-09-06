from flask import Flask, render_template

app = Flask('__name__')



@app.route('/')
def home():
    name = "my name is Slim Shady"
    return f'Hi {name}'

app.run(host='0.0.0.0',port=5000, debug=True)