from flask import Flask, render_template, request, redirect
from API import database

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

# Update의 일부
# database.py의 datas함수로 번호에 해당하는 기존 글 가져오기
# database.py의 update함수 호출 및 갱신

@app.route('/update', methods=['GET'])
def update():
  ups = request.args.get('no')
  total = database.datas(str(ups))
  return render_template('update.html', total= total)

@app.route('/posts1', methods=['POST'])
def posts1():
  no = request.form['no']
  num = str(no)
  ids = request.form['ids']
  title = request.form['title']
  content = request.form['content']
  database.update(num, ids, title, content)
  return redirect('/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)