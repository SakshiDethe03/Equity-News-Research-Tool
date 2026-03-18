<h2>📊 Equity News Research Tool</h2>

An AI-powered research tool that allows users to analyze multiple news articles and ask questions based on their content. The application uses LLMs + Vector Search (FAISS) to provide accurate, source-backed answers.

<img width="1919" height="981" alt="Screenshot 2026-03-17 222034" src="https://github.com/user-attachments/assets/d0130732-1c1e-4e06-bf59-e29fccd40bbe" />

<h4>🚀 Features</h4>

<ul>
  
<li>🔗 Input multiple news article URLs</li>

<li>📄 Automatic content extraction from articles</li>

<li>✂️ Smart text chunking using LangChain</li>

<li>🧠 Semantic search using embeddings</li>

<li>❓ Ask questions related to the articles</li>

<li>📌 Get answers with source references</li>

<li>⚡ Fast retrieval using FAISS vector database</li>

</ul>

<h4>🛠️ Tech Stack</h4>

<ul>
<li>Frontend: Streamlit</li>

<li>LLM: OpenRouter (Nemotron model)</li>

<li>Framework: LangChain</li>

<li>Embeddings: OpenAI Embeddings (via OpenRouter)</li>

<li>Vector DB: FAISS</li>

<li>Language: Python</li>
</ul>

<h4>📂 Project Structure</h4>

EquityNewsResearchTool/<br>
│── main.py<br>
│── faiss_index/        # Saved vector database<br>
│── key.py              # API key file<br>
│── requirements.txt<br>
│── README.md<br>

<h4>⚙️ Installation</h4>

1. Clone the repository
<div style="background:white, border:white 1px solid, padding:50px, 0px">
git clone https://github.com/your-username/equity-news-research-tool.git <br>
cd equity-news-research-tool
</div>

2. Install dependencies <br>
pip install -r requirements.txt <br>

3. Add your API Key <br>
Create a file named key.py: <br>
api_key = "your_openrouter_api_key" <br>

<h4>▶️ Run the Application</h4>
streamlit run main.py <br>

<h4>🧪 How It Works</h4>
<ol>
<li>User enters news article URLs</li>

<li>App loads and extracts content from URLs</li>

<li>Text is split into smaller chunks</li>

<li>Embeddings are created for each chunk</li>

<li>FAISS stores these embeddings locally</li>

<li>User asks a question</li>

<li>System retrieves relevant chunks and generates an answer using LLM</li>
</ol>

<h4>📸 Workflow</h4>
URLs → Load Data → Split Text → Create Embeddings → Store in FAISS
      → User Query → Retrieve Relevant Data → LLM → Answer + Sources<br>
      
<h4>⚠️ Important Notes</h4>

❌ Do NOT use pickle for saving FAISS (causes errors) <br>

✅ Use save_local() and load_local() for persistence <br>

Ensure valid URLs for proper data extraction <br>

<h4>🔮 Future Improvements</h4>

💬 Chat-based UI (like ChatGPT)

⚡ Caching for faster performance

🌐 Support for more than 3 URLs

📊 Summarization of articles

📁 Upload PDF/Docs support

<h4>🙌 Use Case </h4>
<ul>
<li>Financial news analysis</li>

<li>Stock market research</li>

<li>Academic research</li>

<li>Quick insights from multiple sources</li>
</ul>

<h4>👩‍💻 Author</h4>

<b>Sakshi Dethe</b>
B.Tech CSD (AI Engineer)

⭐ If you like this project

Give it a star ⭐ and share it!
