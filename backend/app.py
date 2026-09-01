from multiprocessing import connection
import mysql.connector
from flask import Flask, jsonify



app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
           user = 'root',
              password = 'Creta@1635',
                 database = 'book_management' 
     )
    return connection


    
@app.route("/")
def home():
    return "Book Management API is running"


@app.route("/test-db")
def test_db():
    connection = get_db_connection()

    if connection.is_connected():
        connection.close()
        return "Database connection successful!"

    return "Database connection failed!"


@app.route("/books")
def get_books():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(books)



if __name__ == "__main__":
    app.run(debug=True)