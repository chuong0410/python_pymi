from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('familug1.db', check_same_thread=False)
c = conn.cursor()
pythons = c.execute(
    '''SELECT * FROM familug WHERE label="Python" ''').fetchall()
commands = c.execute(
    '''SELECT * FROM familug WHERE label="Command" ''').fetchall()
sysadmins = c.execute(
    '''SELECT * FROM familug WHERE label="sysadmin" ''').fetchall()
lastests = c.execute(
    '''SELECT * FROM familug WHERE label="Lastest" ''').fetchall()


@app.route('/')
def template():
    return render_template('index.html', pythons=pythons,
                           commands=commands, sysadmins=sysadmins,
                           lastests=lastests)


if __name__ == "__main__":
    app.run(debug=True)
