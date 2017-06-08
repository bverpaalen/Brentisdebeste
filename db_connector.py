import mysql.connector as connector

def db_connect():
    database = connector.connect(host = "localhost",
                               user = "owe8_1617_gr12",
                               passwd = "blaat1234",
                               db = "owe8_167_gr12_2")
    return database

def createConnection():
    connection = database.connect()
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

database = db_connect()
SubmitSearchWord("test")
