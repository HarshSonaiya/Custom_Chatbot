from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from app.loader import load_course_data
from app.embeddings import create_embeddings, load_embeddings, store_embeddings
import numpy as np

app = Flask(__name__)
api = Api(app)

# Load course data and create embeddings
url = "https://brainlox.com/courses/category/technical"
course_texts = load_course_data(url)
embeddings = create_embeddings(course_texts)
store_embeddings(embeddings, "course_embeddings.index")  # Store embeddings for future use

class Chatbot(Resource):
    def get(self):
        return {'message': 'Chatbot API is live!'}, 200

    def post(self):
        data = request.get_json()
        query = data.get('query', '')

        # Process the query and return a response
        # Example: find closest embeddings to query and return relevant information
        index = load_embeddings("course_embeddings.index")
        query_embedding = create_embeddings([query])[0]
        distances, indices = index.search(np.array([query_embedding]), 5)

        # Example response
        response = {'query': query, 'results': []}
        for idx in indices[0]:
            response['results'].append(course_texts[idx])

        return jsonify(response), 200

# Add resource to the API
api.add_resource(Chatbot, '/chatbot')

if __name__ == '__main__':
    app.run(debug=True)
