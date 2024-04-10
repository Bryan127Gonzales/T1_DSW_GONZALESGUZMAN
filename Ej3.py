from flask_script import Manager
from flask import Flask

app = Flask(__name__)
manager = Manager(app) #crea un objeto Manager asociado a la aplicación Flask app.


@app.route('/')
def index():
    return '<h1>Hola mundo cruel!</h1>'

@app.route('/user/<name>')
def user(name):
 return '<h1>Hello, %s!</h1>' % name
if __name__ == '__main__':
    app.run(debug=True)