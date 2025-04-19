import mysql.connector
from mysql.connector import Error

host = 'mysql' 
database = 'db_corre_ai'
user = 'aline'
password = 'correai01'

try:
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        print("Conexão bem-sucedida ao banco de dados MySQL!")

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name, email FROM person")
        rows = cursor.fetchall()

        for row in rows:
            print(f"ID: {row['id']} - Name: {row['name']} - Email: {row['email']}")

except Error as e:
    print(f"Erro na conexão: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
