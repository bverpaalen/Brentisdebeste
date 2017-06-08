import mysql.connector as connector

def main():
    db_connect()

def db_connect():
    database = connector.connect(host = "localhost",
                               user = "owe8_1617_grp12",
                               passwd = "blaat1234",
                               db = "cytosine.nl")
    cursor = database.cursor()
    add_PubMedID = ("INSERT INTO Article"
                    "(PubMed_ID, Previe_summary)"
                    "Values(%s, %s)")
    cursor.execute(add_PubMedID)
    database.commit()
    cursor.close()

main()
