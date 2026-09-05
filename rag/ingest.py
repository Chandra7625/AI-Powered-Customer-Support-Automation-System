import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


# Project root
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

DOC_FOLDER = os.path.join(BASE_DIR, "docs")

print("Loading Textfiles...")

documents = []

for file in os.listdir(DOC_FOLDER):

    if file.endswith(".txt"):

        path = os.path.join(DOC_FOLDER, file)

        loader = TextLoader(path)

        documents.extend(loader.load())


print("Splitting Documents...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")


print("Loading Embedding Model...")

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

print("Creating Vector Database...")

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="vectorstore"
)

print("Vector DB Created Successfully")