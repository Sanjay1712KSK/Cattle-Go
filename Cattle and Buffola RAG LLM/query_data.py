# query_data.py
import argparse
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate

CHROMA_PATH = "chroma_db"

# Custom prompt template
PROMPT_TEMPLATE = """
You are a professional AI assistant. Answer in a human-like manner.
Answer the question using ONLY the information provided in the context.
If the answer is not in the context, answer based on your own knowledge.

Context:
{context}

Question: {question}

Answer:
"""

def query_db(query_text: str):
    # Local embeddings for retrieval
    embedding_function = OllamaEmbeddings(model="nomic-embed-text")

    # Load DB with embedding_function for query embedding computation
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    retriever = db.as_retriever()

    # Local LLM
    llm = OllamaLLM(model="gemma3:12b")

    # Custom prompt
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

    # RetrievalQA chain using the prompt
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )

    # Query the database
    result = qa.invoke({"query": query_text})

    print("\nAnswer:\n", result["result"])
    print("\nSources:")
    for doc in result["source_documents"]:
        print("-", doc.metadata.get("source", "Unknown"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The question to ask the DB")
    args = parser.parse_args()
    query_db(args.query_text)




# ollama serve
# python create_database.py
# python query_data.py "Tell me about Pandharpuri buffalo"
