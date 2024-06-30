from app.loader import load_course_data
from app.embeddings import create_embeddings, store_embeddings

urls = [
    "https://brainlox.com/courses/category/technical"
]

course_texts = load_course_data(urls)
print(load_course_data(urls))
embeddings = create_embeddings(course_texts)
store_embeddings(embeddings, "course_embeddings.index")

print("Course data and embeddings are ready!")
