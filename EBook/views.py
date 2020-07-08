from flask import request, jsonify 
from EBook import app, db
from EBook.models import Book, book_schema, books_schema


@app.before_first_request
def create_table():
    db.create_all()
    # db.drop_all()
    
#create a new book
@app.route('/book', methods=['POST'])
def add_book():
    data=request.get_json(force=True)
    title=data['title']
    description=data['description']
    author=data['author']
    price=data['price']
  
    new_book = Book(title, description, author, price)
    
    db.session.add(new_book)
    db.session.commit()
    return book_schema.jsonify(new_book)

#get all books
@app.route('/book', methods=['GET'])
def get_books():
    all_books = Book.query.all()
    record = books_schema.dump(all_books)
    return jsonify(record)

#get a single book
@app.route('/book/<id>', methods=['GET'])
def get_book(id):
    book = Book.query.get(id)
    return book_schema.jsonify(book)

#update a book
@app.route('/book/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    data=request.get_json(force=True)
    title=data['title']
    description=data['description']
    author=data['author']
    price=data['price']
  
    book.title = title
    book.description = description
    book.author = author
    book.price = price
        
    db.session.commit()
    
    return book_schema.jsonify(book)

#delete a book
@app.route('/book/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    
    return book_schema.jsonify(book)
      
    
    


    

      
    






