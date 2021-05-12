from flask import Flask
from API import database

app = Flask(__name__)

@app.route('/')
def home():
    a = database.dbconnect()
    return a

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)