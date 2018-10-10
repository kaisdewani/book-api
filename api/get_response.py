import json
from flask import Flask, Response, abort 
from .utils import JSON_MIME_TYPE

app = Flask(__name__)

books = [{
  'id' : 1,
  'title' : 'Harry Potter 1',
  'author_id' : 1
}]

@app.route('/books')
def book_list():
  responce = Response(
    json.dumps(books), status=200, mimetype= JSON_MIME_TYPE)
  return responce
