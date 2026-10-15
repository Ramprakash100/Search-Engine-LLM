import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import (
    ArxivAPIWrapper,
    WikipediaAPIWrapper,
)
from langchain_community.tools import (
    ArxivQueryRun,
    WikipediaQueryRun,
    DuckDuckGoSearchRun,
)
from langchain_classic.agents import initialize_agent, AgentType
from langchain_classic.callbacks import StreamlitCallbackHandler

# -------------------- Tools --------------------

arxiv_wrapper = ArxivAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=200,
)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=200,
)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name="Search")

tools = [search, arxiv, wiki]

# -------------------- Streamlit UI --------------------

st.title("🔎 LangChain - Chat with Search")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input(
    "Enter your Groq API Key:",
    type="password",
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I'm a chatbot who can search the web. How can I help you?",
        }
    ]

# Display conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# -------------------- Chat --------------------

if prompt := st.chat_input("What is machine learning?"):

    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar.")
        st.stop()

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    st.chat_message("user").write(prompt)

    try:
        llm = ChatGroq(
            groq_api_key=api_key,
            model_name="openai/gpt-oss-120b",
            temperature=0,
            streaming=False,
        )

        search_agent = initialize_agent(
            tools=tools,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True, 
        )

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(
                st.container(),
                expand_new_thoughts=False,
            )

            response = search_agent.invoke(
                {"input": prompt},
                config={"callbacks": [st_cb]},
            )

            answer = response["output"]
            st.write(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")
