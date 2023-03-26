import mysql.connector
mybd = mysql.connector.connect(host = "localhost",
                            user = "root",passwd = "Prakash@123")
courser = mybd.cursor()

