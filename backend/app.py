import mysql.connector
from flask import Flask, jsonify, request



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


@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()

    title = data["title"]
    author = data["author"]
    published_year = data["published_year"]

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO books (title, author, published_year)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (title, author, published_year))
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Book added successfully!"
    }), 201


if __name__ == "__main__":
    app.run(debug=True)