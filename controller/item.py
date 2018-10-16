from flask_restful import Resource, reqparse

from model.item import ItemModel


class ItemController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store id"
                        )

    def get(self, name):
        item = ItemModel.find_by_name(name)
        return item.json() if item else {'mesage': 'An item with a name {} did not exists'.format(name)}

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "An item with the name {} already exists".format(name)}, 400

        payload = ItemController.parser.parse_args()
        item = ItemModel(name, **payload)
        try:
            item.save_to_db()
        except:
            return {"message": "An error ocurred while inserting the item"}, 500

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item is None:
            return {'message': 'Item with name {} not found'.format(name)}, 400
        item.delete_from_db()
        return {'message': 'Item deleted'}

    def put(self, name):
        payload = ItemController.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **payload)
        else:
            item.price = payload.get('price')

        item.save_to_db()

        return item.json()


class ItemListController(Resource):

    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}, 200
