import os

from api.get_method import app

if __name__ == '__main__':
    app.debug = True
    # DATABASE_NAME is set to library.db schema
    app.config['DATABASE_NAME'] = 'library.db'
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)