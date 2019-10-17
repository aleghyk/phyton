#flask framework
#modules : pytest, request, flask, flask-RESTful
#pip freeze >requirements.txt //pip install -r requirements.txt


from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
@app.route('/', methods['post']) //reaction on get context "/" 
def index():
    return "Hello!"
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('id')   

class Patiens(Resource):
    def get(self, pid):
#        args =parser.parse_args()
        db = SQ.connect('test.db')
        db.execute('select name from a where id=?', (pid,))
        db.commit()
        db.close()
        return args1['id'], 201 
    def delete(self, pid):
        db = SQ.connect('test.db')
        db.execute('delete from a where id=?', (pid,))
        db.commit()
        db.close()
        return args1['id'], 204
    def update(self, pid):
        db = SQ.connect('test.db')
        db.execute('update from a where id=?', (pid,))
        db.commit()
        db.close()
        return args1['id'], 201
   

class PatientList (Resource):
    def post(self):
        args =parser.parse_args()
        db = SQ.connect('test.db')
        db.execute('insert into a (id, name) values (?, ?)', {args['id'], args['name']})
        db.commit()
        db.close()
        return args1['id'], 201
     def get(self, pid):
        db = SQ.connect('test.db')
        db.execute('select id,name from a', (pid,))
        db.commit()
        db.close()
        return rows
api.add_resource(PatientList, '/patients')
app.run(debug=true)

 


