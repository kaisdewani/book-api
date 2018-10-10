import json
from flask import Flask, Response, abort 
from .utils import JSON_MIME_TYPE

app = Flask(__name__)

#hard code list of books 
books = [{
  'id' : 1,
  'title' : 'Harry Potter 1',
  'author_id' : 1
},
{
  'id' : 2,
  'title' : 'Lord of the Rings',
  'author_id' : 2
}]

@app.route('/books', methods=['GET'])
def book_list():
  #create flask response that will convert books list into json and return it along with 200 response code
  #mime type allows for content type to be rendered
  response = Response(
    json.dumps(books), status=200, mimetype= JSON_MIME_TYPE)
  return response


@app.route('/books/<int:book_id>', methods=['GET'])
def book_detail(book_id):
  book = search_book(books, book_id)
  if book is None:
    abort(404)
  
  content = json.dumps(book)
  return content, 200, {'Content-Type': JSON_MIME_TYPE}



def search_book(books, book_id):
  for book in books:
    if book['id'] == book_id:
      return book





# not working
# testing it out
# def search_by_title(books, book_title):
#   for book in books:
#     if book['title'] == book_title:
#       return book

# @app.route('/books/<str:book_title>')
# def book_title(book_title):
#   book = search_by_title(books, book_title)
#   if book is None:
#     abort(404)
  
#   content = json.dumps(book)
#   return content, 200, {'Content-Type': JSON_MIME_TYPE}