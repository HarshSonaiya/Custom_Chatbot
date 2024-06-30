from flask import Flask
from flask_restful import Api
from app.api import QueryCourse

app = Flask(__name__)
api = Api(app)

api.add_resource(QueryCourse, '/')

if __name__ == '__main__':
    app.run(debug=True)
