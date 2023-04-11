from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('home-banking.html', saludo = persona1.saludo() )

@app.route('/saludo')
def home():#aca pongo que es lo que quiero que me devuelva cuando yo entro al home de mi pagina

    return render_template('index.html', saludo = persona1.saludo() ) # le digo que me renderize tal html con la informacion de la variable saludo

if __name__ == '__main__':
    from persona import Persona 
    persona1 = Persona(32456756,'sabrina') #aca creamos un objeto persona

    app.run(debug=True)    #aca es donde arranca el programa