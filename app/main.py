from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

vectorstore_path = "../vectorstore/faiss_index"

#Load embeddings
embeddings = OllamaEmbeddings(model='nomic-embed-text')

#Load vectorstore
vectorstore = FAISS.load_local(vectorstore_path,embeddings,allow_dangerous_deserialization=True)

#Build retriever
retriever = vectorstore.as_retriever(search_type = "similarity", search_kwargs = {"k":20})

#Choose model
model = init_chat_model("gemma3:4b",model_provider="ollama")

system_prompt = ("You are an assistant for question-answering tasks. "
                "Use the following pieces of retrieved context to answer "
                "the question. If you don't know the answer, say that you "
                "don't know. Make the answer as detailed as needed for clarity. "
                "You must ONLY answer based on the provided context." 
                "If the context does not contain enough information, you must say 'I don't know.' "
                "Do NOT generate external links, external examples, or extra references." 
                "\n\n{context}")



#Create prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

#Create RAG chain
question_answer_chain = create_stuff_documents_chain(model,prompt)
rag_chain = create_retrieval_chain(retriever,question_answer_chain)


#Ask a question from the assistant

user_question = input("Your question: ")


results = rag_chain.invoke({"input": user_question})

print("\n Assistant's Answer:")
print(results["answer"])

