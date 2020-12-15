import json
from flask import Blueprint
from flask import request,g,current_app,jsonify
from models import MyData
from app import db

bp = Blueprint('api', __name__)


@bp.route('/')
def hello_world():
    return 'Hello, World!'


@bp.route('/test', methods=['GET'])
def test():
    return 'test'


@bp.route('/update-data', methods=['POST'])
def update_data():
    json_data = request.get_json('data')
    name = json_data.get('name')
    data = json.dumps(json_data.get('data'))

    mydata = MyData.query.filter_by(username=name).first()
    if mydata is None:
        mydata = MyData(username=name, data=data)
    else:
        mydata.data = data
    db.session.add(mydata)
    db.session.commit()
    return 'ok', 200

@bp.route('/get-datas', methods=['GET'])
def get_datas():
    name = request.args.get('name')
    data = MyData.query.filter_by(username=name).first_or_404()
    return jsonify(data.data)