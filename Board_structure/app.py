from flask import Flask, render_template, request, redirect
from API import db

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/board')
def board():
  b = db.read()
  for i in range(0, len(b)):
    for j in range(0, len(b)):
      if(i < j):
        temp = b[i]
        b[i] = b[j]
        b[j] = temp
  return render_template('main.html', b=b)

@app.route('/create')
def create():
  return render_template('Create.html')

@app.route('/post1', methods=['POST'])
def post1():
  ids = request.form['ids']
  title = request.form['title']
  content = request.form['content']
  db.create(ids, title , content)
  return redirect('/board')

@app.route('/read', methods=['GET'])
def read():
  no = request.args.get('no')
  total = db.datas(str(no))
  return render_template('read.html', total = total)

@app.route('/update', methods=['GET'])
def update():
  ups = request.args.get('no')
  total = db.datas(str(ups))
  return render_template('update.html', total= total)

@app.route('/posts1', methods=['POST'])
def posts1():
  no = request.form['no']
  num = str(no)
  ids = request.form['ids']
  title = request.form['title']
  content = request.form['content']
  a = db.update(num, ids, title, content)
  return redirect('/board')

@app.route('/delete')
def delete():
  dels = request.args.get('no')
  db.delete(str(dels))
  return redirect('/board')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)

# 오류 발견시 피드백 및 즉시 수정예정