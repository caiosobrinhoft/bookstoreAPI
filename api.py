from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 0,
        'titulo': 'Percy Jackson',
        'autor': 'Rick Riordan'
    },
    {
        'id': 1,
        'titulo': 'Harry Potter',
        'autor': 'J.K Rowling'
    },
    {
        'id': 2,
        'titulo': 'Hunger Games',
        'autor': 'Suzanne Collins'
    },
]

#Consult all
@app.route('/books',methods=['GET'])
def obtainBooks():
    return jsonify(books)

#Consult by id
@app.route('/books/<int:id>',methods=['GET'])
def obtainBooksById(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

#Edit
@app.route('/books/<int:id>',methods=['PUT'])
def editBookById(id):
    new_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(new_book)
            return jsonify(books[index])
        
#Create
@app.route('/books',methods=['POST'])
def newBook():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)

#Delete
@app.route('/books/<int:id>',methods=['DELETE'])
def deleteBook(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]

    return jsonify(books[index])
        
app.run(port=5000, host='localhost', debug=True)