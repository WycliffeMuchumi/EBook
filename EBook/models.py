from EBook import db, ma

#This is the book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    author = db.Column(db.String(100))
    price = db.Column(db.Float)
    
    def __init__(self, title, description, author, price):
      self.title = title
      self.description = description
      self.author = author
      self.price = price
      
#Book schema
class BookSchema(ma.Schema):
    class Meta:
        fields = ('id','title', 'description','author','price')
        
#initialize schema(when dealing/fetching a single book)
book_schema = BookSchema()
#initialize schema(when dealing/fetching  many books)
books_schema = BookSchema(many=True)

        
              
         
    
    
