import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/mydata.db'
db = SQLAlchemy(app)
db.init_app(app)



@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test', methods=['GET'])
def test():
    return 'test'


@app.route('/update', methods=['POST'])
def data_update():
    json_data = request.get_json('data')
    name = json_data.get('name')
    data = json.dumps(json_data.get('data'))
    print(data)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)


# -i https://pypi.tuna.tsinghua.edu.cn/simple
