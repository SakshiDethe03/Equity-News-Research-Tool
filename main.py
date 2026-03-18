import os
import streamlit as st
import time
from langchain_openai import ChatOpenAI
from langchain_classic.chains import RetrievalQAWithSourcesChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    temperature=0.6
)

st.title("Equity News Research Tool 📈")
st.sidebar.title("News Article URLs 🔗")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    if url.strip() != "":
        urls.append(url)
        
process_url_clicked = st.sidebar.button("Process URLs")

main_placeholder = st.empty()

# ================= PROCESSING =================
if process_url_clicked:
    if not urls:
        st.warning("Please enter at least one URL")
    else:
        loader = UnstructuredURLLoader(urls=urls)
        main_placeholder.text("Data Loading...Started...✅")
        data = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000,
        )
        main_placeholder.text("Text Splitting...Started...✅")
        docs = text_splitter.split_documents(data)

        embeddings = OpenAIEmbeddings(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
       )

        vectorstore_openai = FAISS.from_documents(docs, embeddings)
        main_placeholder.text("Embedding Done...✅")
        time.sleep(2)

        vectorstore_openai.save_local("faiss_index")


# ================= QUERY =================
query = st.text_input("Enter your question about the news articles:")

if query:
    if os.path.exists("faiss_index"):

        embeddings = OpenAIEmbeddings(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

        vectorstore = FAISS.load_local(
            "faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )

        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
        )

        result = chain({"question": query}, return_only_outputs=True)

        st.header("Answer:")
        st.write(result['answer'])

        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")
            for source in sources_list:
                st.write(source)
