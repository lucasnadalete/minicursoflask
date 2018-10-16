from flask import Flask
from flask_restful import Api
from controller.item import ItemController, ItemListController
from controller.store import StoreController, StoreListController

app = Flask(__name__)

POSTGRES_URI = 'postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}'.format(
    db='d64aoral2b3js8',
    host='ec2-23-21-201-255.compute-1.amazonaws.com',
    port='5432',
    user='elnrwwmposjwkx',
    pw='99e87646a577d4f21c36b7d8bec8a6a0bfde8b5218d5e27d9d51c589569c52e1'
)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
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
