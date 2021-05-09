from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/test')
def hello():
    return render_template('get.html')
 
@app.route('/get', methods=['GET'])
def get():
    receive = request.args['data']
    gets = request.args.get('gets')
    return gets

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
