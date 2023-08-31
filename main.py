from flask import Flask, render_template, request
import sqlite3
from sre_constants import SUCCESS, FAILURE



app = Flask(__name__)

def connect_to_db() -> sqlite3.Connection:
    conn = sqlite3.connect("sqlite3db.db")
    return conn
#conn.execute('SELECT * FROM users')

@app.get("/")
def homepage() -> str:
    try:
        con = connect_to_db()
        con.execute('''
        CREATE TABLE users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstName TEXT NOT NULL,
            lastName TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
        ''')
        con.commit()
        con.close()
        
        return str(SUCCESS)
    except sqlite3.Error as e:
        return str(e)

@app.get("/submit")
@app.post("/submit")
def submit_data() -> str:
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']

        try:
            con = connect_to_db()
            con.execute('''
            CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
            );
            ''')
            # insert data into db
            con.execute("INSERT INTO users(firsname, lastname, email) VALUES(?,?,?)""", (firstname, lastname, email))
            con.commit()
            con.close()
            return str(SUCCESS)
        except sqlite3.Error as e:
            print(str(e))
            return str(FAILURE) + "-> DB failed to store data "
        
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5555)
