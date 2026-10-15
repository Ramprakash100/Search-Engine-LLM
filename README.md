# 🔎 LangChain Chat with Search

An AI-powered research chatbot built with **Streamlit, LangChain, and Groq**. It answers user questions by leveraging external tools to search the web, retrieve information from Wikipedia, and find academic research papers on arXiv.

## 🚀 Features

- **AI-Powered Chat:** Interact with a language model using natural language.
- **Web Search:** Retrieve relevant information from the web using DuckDuckGo.
- **Wikipedia Search:** Retrieve concise information about topics from Wikipedia.
- **Research Paper Search:** Find academic papers using the arXiv API.
- **Tool-Calling Agent:** Uses LangChain's agent framework to select and execute tools when needed.
- **Interactive UI:** Chat interface built with Streamlit.
- **Secure API Key Input:** Enter your Groq API key through a password-protected sidebar field.
- **Conversation History:** Display messages from the current Streamlit session.

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- LangChain Community
- LangChain Groq
- Groq API
- DuckDuckGo Search
- Wikipedia API
- arXiv API

## 📁 Project Structure

```text
langchain-chat-with-search/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/langchain-chat-with-search.git
cd langchain-chat-with-search
```

Replace `YOUR_USERNAME` with your GitHub username and use your actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you have not created `requirements.txt` yet, install the required packages:

```bash
pip install streamlit langchain langchain-community langchain-groq langchain-classic langgraph ddgs arxiv wikipedia
```

### 4. Get a Groq API key

Obtain an API key from the [Groq Console](https://console.groq.com/).

Launch the application and enter your API key in the sidebar. Never commit your API key to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💬 How to Use

1. Launch the Streamlit application.
2. Enter your Groq
