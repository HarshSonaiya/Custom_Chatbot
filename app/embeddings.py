import openai
import faiss
import numpy as np
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_embeddings(texts):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=texts
    )
    embeddings = [data['embedding'] for data in response['data']]
    return embeddings

def store_embeddings(embeddings, file_path):
    embeddings_array = np.array(embeddings)
    index = faiss.IndexFlatL2(embeddings_array.shape[1])
    index.add(embeddings_array)
    faiss.write_index(index, file_path)

def load_embeddings(file_path):
    return faiss.read_index(file_path)
