from flask import Flask #importa la clase Flask del módulo flask
app = Flask(__name__)#crea una instancia de la clase Flask 
@app.route('/')#Decorador, define una ruta para la aplicación.
def index(): #función que será ejecutada cuando se acceda a la ruta principal ('/')
    return '<h1>Hola mundo cruel!</h1>' #Devuelve una cadena de texto
if __name__ == '__main__': #verifica si el script está siendo ejecutado como el programa principal
    app.run(debug=True)#inicia el servidor de desarrollo de Flask