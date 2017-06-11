from flaskext.mysql import MySQL
from flask import Flask

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'owe8_1617_gr12'
app.config['MYSQL_DATABASE_PASSWORD'] = 'blaat1234'
app.config['MYSQL_DATABASE_DB'] = 'owe8_1617_gr12_2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def createConnection():
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

def SubmitArticle(ListOfArticle):
    connection = createConnection()
    cursor = createCursor(connection)
    #Input should be a tuple of article information gathered into a list
    #[(information,etc.)(information,etc.)]
    cursor.executemany("INSERT INTO Article(PubMed_ID,Article_link,Author,Date,Preview_summary,Search_Keywords_ID) VALUES (%s,%s,%s,%s,%s,%s)",ListOfArticle)
    submitCursor(cursor,connection)

def LinkArticelWithSearchWord(Links):
    connection = createConnection()
    cursor = createCursor(connection)
    cursor.executemany("INSERT INTO //TABLE//(id,id)VALUES(%s,%s)",Links)
    submitCursor(cursor,connection)

def SearchWordId(searchword):
    connection = createConnection()
    cursor = createCursor(connection)
    cursor.execute("SELECT Keywords_ID FROM SEARCH WHERE Keywords=%s",searchword)
    for item in cursor:
        print(item)

print(SearchWordId("zoekwoordje"))
