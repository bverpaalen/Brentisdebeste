from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user="owe8_1617_gr12", database="_1617_gr12_2")
cursor = cnx.cursor()

tomorrow = datetime.now().date()+ timedelta(days=1)

add_Gene = ("INSERT INTO _1617_gr12_2"
                "(Article_has_Gene, Gene)"
                "VALUES(%s, %s)")
add_Article = ("INSERT INTO _1617_gr12_2"
               "(Article, Organism, Search)"
               "VALUES(%s, %s, %s)")
add_StressEnvironment = ("INSERT INTO _1617_gr12_2"
            "(Stress_environment, Stress_environment_has_Article, Stress_environment_has_Organism)"
                         "VALUES(%s, %s, %s)")
#Insert new Article
cursor.execute(add_Article, Article)
art_no = cursor.lastrowid

#Insert Gene informaticn
cursor.execute(add_Gene, Gene)

#bevestigen dat de data comitted is met de database
cnx.commit()
cursor.close()
cnx.close()
