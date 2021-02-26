from app import *
import mysql.connector as mysql

HOST = "127.0.0.1"
DATABASE = "birthdays"
USER = "remote-user"
PASSWORD = "n5qD@H&KL"
db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)

print("\nConnected to:", db_connection.get_server_info(),"\n")

mycursor = db_connection.cursor()
mycursor.execute("SELECT * FROM dinners")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)