from flask import Flask, render_template, request, redirect
from API import korea

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')


# 삭제의 일부 기능만 구현
# 삭제 API 호출
# 글 번호를 따로 불러와야 함

@app.route('/delete')
def delete():
  dels = request.args.get('no')
  korea.delete(str(dels))
  return redirect('/board_kr')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)