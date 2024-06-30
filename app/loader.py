from langchain_community.document_loaders import UnstructuredURLLoader

def load_course_data(url):
    loader = UnstructuredURLLoader(urls=url)
    data = loader.load()    
    return data
