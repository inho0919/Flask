from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/test')
def hello():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def post():
    receive = request.form['test']
    return receive

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
