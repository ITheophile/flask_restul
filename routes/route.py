from flask_restful import Resource, abort
import uuid
from datetime import datetime


# todos = { uuid.uuid4().int: {
#     'title': 'learn python',
#     'description': 'learn the basics of python',
#     'done':False,
#     'createdAt': datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S"),
#     'updatedAt':datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")
#     }
#     }

todos = {}

class Default(Resource):
    def get(self):
        return {'todos': todos}


        
class TodoSingle(Resource):

    def get(self, todo_id):
        if todo_id not in todos:
            return {'message': "task doesn't exit!"}, 404
        return {todo_id: todos[todo_id]}, 202

    # def post(self):
        # todo_id = uuid.uuid4().int




