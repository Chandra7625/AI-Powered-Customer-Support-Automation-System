from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

db = Chroma(
    persist_directory="vectorstore",
    embedding_function=embeddings
)

def retrieve(query):

    docs = db.similarity_search(
        query,
        k=3
    )

    context = ""

    for doc in docs:
        context += doc.page_content + "\n\n"

    return context