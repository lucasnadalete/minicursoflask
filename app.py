from flask import Flask
from flask_restful import Api
from controller.item import ItemController, ItemListController
from controller.store import StoreController, StoreListController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATONS'] = False
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(ItemController, '/item/<string:name>')
api.add_resource(ItemListController, '/items')
api.add_resource(StoreController, '/store/<string:name>')
api.add_resource(StoreListController, '/stores')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(host='0.0.0.0', debug=True, port=80)
