from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET'])
def register():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def endpoint():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
    db.commit()
    db.close()

    return render_template('index.html')

# init database
# db = sqlite3.connect('database.db')
# cursor = db.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL,
#         email TEXT NOT NULL,
#         password TEXT NOT NULL
#     )
# ''')
# db.commit()

# #update user
# db = sqlite3.connect('database.db')
# cursor = db.cursor()
# name = "Ege Kibar"
# email = "ege@kibar.dev"
# password = "12345678"
# user_id = 1
# cursor.execute('UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s', (name, email, password, user_id))
# db.commit()

# #delete user
# db = sqlite3.connect('database.db')
# cursor = db.cursor()
# cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
# db.commit()
# db.close()

if __name__ == '__main__':
    app.run(debug=True)