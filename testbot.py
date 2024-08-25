from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


llm = Ollama(model='llama2')
embeddings = OllamaEmbeddings()

docs = [
    Document(page_content='Zenless zone zero', metadata={'Developer': 'Mihoyo', 'Type': 'Role Playing Game'}),
]

vectordb = FAISS.from_documents(docs, embeddings)
retriever = vectordb.as_retriever()

prompt = ChatPromptTemplate.from_messages([
    ('system', 'Answer the user\'s questions based on the context provided below:\n\n{context}'),
    ('user', 'Question: {input}'),
])
document_chain = create_stuff_documents_chain(llm, prompt)

retrieval_chain = create_retrieval_chain(retriever, document_chain)

context = []
input_text = input('>>> ')
while input_text.lower() != 'bye':
    response = retrieval_chain.invoke({
        'input': input_text,
        'context': context
    })
    print(response['answer'])
    context = response['context']
    input_text = input('>>> ')