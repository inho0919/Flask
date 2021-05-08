from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/page')
def page():
  return 'Page 페이지'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)

# Created By Inho
