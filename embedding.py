from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma


embeddings = OpenAIEmbeddings()
with open("apitable_toolkit/tool/tool_prompt.txt") as f:
    tool_prompts = f.read()
text_splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)
texts = text_splitter.create_documents([tool_prompts])
db = Chroma.from_documents(texts, embeddings, persist_directory="./db")
db.persist()
