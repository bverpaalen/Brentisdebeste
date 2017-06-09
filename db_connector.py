from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'owe8_1617_gr12'
app.config['MYSQL_DATABASE_PASSWORD'] = 'blaat1234'
app.config['MYSQL_DATABASE_DB'] = 'owe8_1617_gr12_2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def db_connect():
    database = connector.connect(host = "localhost",
                               user = "owe8_1617_grp12",
                               passwd = "blaat1234",
                               db = "owe8_167_gr12_2")
    return database

def createConnection():
    #connection = database.connect()
    connection = mysql.connect()	    
    return connection

def createCursor(connection):
    cursor = connection.cursor()
    return cursor

def infoCursor(cursor,connection):
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

def submitCursor(cur,con):
    con.commit()
    cur.close()
    con.close()

def SubmitSearchWord(searchWord):
    connection = createConnection()
    cursor = createCursor(connection)
    cursor.execute("INSERT INTO Search VALUES (NULL,%s)",searchWord)
    submitCursor(cursor,connection)

SubmitSearchWord("test")
