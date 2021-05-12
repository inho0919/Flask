from flask import Flask, render_template, request, redirect
from API import database

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/write')
def write():
  return render_template('write.html')

@app.route('/post1', methods=['POST'])
def post1():
  ids = request.form['ids']
  title = request.form['title']
  content = request.form['content']
  database.create(ids, title , content)
  return redirect('/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)