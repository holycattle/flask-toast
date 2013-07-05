import json
from flask import Flask, request
import sqlalchemy
from db/database import db_session, db_init

app = Flask(__name__)
db_init()

if __name__ == '__main__':
  print 'Listening on port 8080'
  app.run(host='0.0.0.0', port=8080, debug=True)
