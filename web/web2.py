from flask import Flask
  
app = Flask(__name__)

port=4000
host='localhost'
@app.route('/')
def home():
    return f'<h1>Hello, Wellcome to Website! Host: {host} Port: {port}</h1>'
if __name__ == '__main__':
    app.run(host=host, port=port, debug=True, ssl_context='adhoc')
