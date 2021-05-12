from flask import Flask, render_template, request, redirect
from API import database

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/board')
def korean():
  b = database.read()
  for i in range(0, len(b)):
    for j in range(0, len(b)):
      if(i < j):
        temp = b[i]
        b[i] = b[j]
        b[j] = temp
  return render_template('board.html', b=b)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)