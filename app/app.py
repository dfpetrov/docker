import os
from flask import Flask
from views import foo, boo

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/', methods = ['GET'])
@app.route('/<int:number>', methods = ['GET'])
def show_post(number=1):
    # return 'number %d' % number
    return foo(number)

@app.route('/rm', methods = ['GET'])
def rm():
    return boo()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
    # app.run(debug = True)