from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
        <!DOCTYPE html>
        <head>
            <title>Prueba</title> 
        </head>
        <body>
            <h1>Hola a todos</h1>
            <p><a href="/pagina2">Ir a la pagina 2</a></p> 

        </body>
        <footer>
            <p>Algo para poner al final de pagina</p>
        </footer>
        </html>
    """

@app.route('/pagina2')
def pagina2():
    return """
        <!DOCTYPE html>
        <head>
            <title>Pagina2</title> 
        </head>
        <body>
            <h1>Hola de nuevo</h1>
            <p><a href="/">Ir a la pagina principal</a></p> 

        </body>
        <footer>
            <p>Pie de pagina/p>
        </footer>
        </html>
    """
if __name__ == '__main__':
    app.run(debug=True)