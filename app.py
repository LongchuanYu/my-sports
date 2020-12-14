from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/mydata.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test', methods=['GET'])
def test():
    return 'test'

# -i https://pypi.tuna.tsinghua.edu.cn/simple

if __name__ == '__main__':
    app.run(debug=True)