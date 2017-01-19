from flask import Flask, render_template, g, request, json
import sqlite3
import os

app = Flask(__name__) #Erstellt die Anwendungs Instanz
app.config.from_object(__name__) #läd die config aus dieser Datei, app.py

#Erstellt die Standardkonfiguration der Datenbank
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'app.db'), #die path variablen werden benutzt um die Datenbak in einer Webanwendung zu finden
    SECRET_KEY='development key', #Secret Key ist zum schützen der Clientseitigen Sessions
    USERNAME='lucas',
    PASSWORD='123'
))
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#==========================================================================================================


conn = sqlite3.connect('sqlite.db')
c = conn.cursor()

#Einfache funktion um die Datenbank zu erstellen
def create_tables():
    c.execute('CREATE TABLE IF NOT EXISTS food(food_id INTEGER PRIMARY KEY AUTOINCREMENT , title TEXT, stock_value REAL)')
    c.execute('CREATE TABLE IF NOT EXISTS orders(order_id INTEGER PRIMARY KEY AUTOINCREMENT, ordered_food_id INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS customers(customer_id INTEGER PRIMARY KEY AUTOINCREMENT, customer_name TEXT, order_id INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT, email TEXT, password TEXT)')




create_tables()
#Diese Methode ermöglicht schnelle, einfache Verbindungen zu der definierten Datenbank
"""
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE']) #springt zu dem Pfad der oben definiert ist
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Datenbank wird initialisiert...')


#Datenbank Verbindung Aufbauen
def get_db():
    #Öffnet eine neue Verbindung wenn noch keine für die aktuelle DB existiert
    if not hasattr(g, 'sqlite.db'):
        g.sqlite_db = connect_db() #g ist ein Objekt in dem man sicher Informationen speichern kann
    return g.sqlite_db


#Datenbank Verbindung trennen
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

"""


#==========================================================================================================

@app.route('/')
def main():
    return render_template('index.html')

#Die Route showSignUp zeigt beim Clicken des Signup Buttons die signup.html Seite an
@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

#Route zum Anzeigen der Login / Anmelden Seite
@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')


#JQuery AJAX schickt die Signup Daten per POST Methode zu dieser Funktion. Hier werden dann die User angelegt
@app.route('/signUp', methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    #Überprüfe ob die Daten valide sind, dafür die Daten in json umwandeln
    if _name and _email and _password:

        conn = sqlite3.connect('sqlite.db')
        c = conn.cursor()

        c.execute("INSERT INTO users(user_name, email, password) VALUES (?, ?, ?)", (_name, _email, _password))
        conn.commit()
        return json.dumps({'html': '<span>Registrierung erfolgreich!</span>'})


    else:
        return json.dumps({'html': '<span>Ungültige Eingabe!</span>'})



if __name__ == '__main__':
    app.run(port=5000)
