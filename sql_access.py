import mysql.connector

cnx = mysql.connector.connect(user='root', password='ZKMHH6vm9wpipQ',
                              host='34.74.33.75',
                              database='wordpress')
cnx.close()

#grant all on *.* to 'wordpress@34.66.79.99' identified b   