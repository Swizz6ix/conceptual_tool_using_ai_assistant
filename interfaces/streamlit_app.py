import streamlit as st
import pandas as pd

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


from agent import run_agent as agent
from utilities import greet
from guardrails import (
    VALID_TOOLS,
    show_dead_letter_queue,
    DEAD_LETTER_QUEUE
)


MAX_ITERATIONS = 5  # Limit the number of iterations to prevent infinite loops

TOOLS = [
    tool["name"]
    for tool in VALID_TOOLS.values()
]

data = pd.DataFrame(
    {
        "Available Tools": TOOLS
    }
)

st.set_page_config(
    page_title = "Conceptual AI Tool-Using Assistant",
    layout="wide"
)

st.title(
    ":red[Conceptual] :orange[Tool] :green[Using] AI :rainbow[Assistant] :blossom:",
    text_alignment = "left"
)

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "history" not in st.session_state:
    st.session_state.history = []

if "iteration" not in st.session_state:
    st.session_state.iteration = 0

if "last_response" not in st.session_state:
    st.session_state.last_response = ""

if "last_json" not in st.session_state:
    st.session_state.last_json = ""


@st.dialog("Hello, I am your AI assistant. What is your name", dismissible = False, on_dismiss="rerun")
def userName():
    user = st.text_input("Enter your name to proceed ")
    if st.button("Submit"):
        st.session_state.user_name = user
        st.rerun()

if st.session_state.user_name == "":
    userName()

# The sidebar
with st.sidebar:
    st.subheader("User")

    with st.container(border=True):
        st.write(
            f":sunglasses: {st.session_state.user_name}"
        )

    if st.session_state.user_name:
        st.success(
            f"{greet()} "
            f"{st.session_state.user_name}"
        )
    st.divider()

    st.subheader("Tools")
    st.dataframe(data, width="stretch", hide_index = True)


col1, col2 = st.columns([1, 3])

with col1:
    st.subheader("User")

    with st.container(border=True):
        st.write(
            f":sunglasses: {st.session_state.user_name}"
        )

    if st.session_state.user_name:
        st.success(
            f"{greet()} "
            f"{st.session_state.user_name}"
        )
    st.divider()

    st.subheader("Tools")
    st.dataframe(data, width="stretch", hide_index = True)

with col2:
    with st.container(border=True, height="stretch"):
        chat_tab, tools_tab, history_tab, dlq_tab, diagnostics_tab = st.tabs([
            "💬 Chat",
            # "🧠 Agent Pipeline",
            "🛠 Available Tools",
            "📜 History",
            "⚠ Dead Letter Queue",
            "⚙ Diagnostics"
        ])


user_name = st.session_state.user_name

with chat_tab:
    prompt = st.chat_input(
        "How can I help you",
    )

    if prompt != None:
        try:
            result = agent(prompt, user_name)

            st.session_state.last_request = prompt
            st.session_state.last_json = result["tool_request"]
            st.session_state.last_response = result["response"]

            st.session_state.history.append({
                "prompt": prompt,
                "response": result["response"]
            })

            st.session_state.iteration += 1
            
            st.json(result['tool_request'])
            st.markdown(result['response'])
                
        except Exception as e:
            st.error(e)

    with tools_tab:
        st.subheader("Registered Tools")

        for tool in VALID_TOOLS.values():
            TOOLS.append(tool["name"])
            with st.expander(tool["name"]):
                st.write(tool["description"])
                st.write(f"requires: {tool["input_format"]}")

with history_tab:
    if not st.session_state.history:
        st.info("No conversation yet.")

    for item in reversed(st.session_state.history):
        st.chat_message("user").write(item["prompt"])
        st.chat_message("assistant").write(item["response"])

with dlq_tab:
    st.subheader("Dead Letter Queue")

    if st.button("click to show Failed request"):
        dlq = show_dead_letter_queue()
        
        df = pd.json_normalize(dlq)
        st.dataframe(df, use_container_width=True)

with diagnostics_tab:
    st.metric(
        "Iteration",
        st.session_state.iteration
    )

    st.metric(
        "Conversation Length",
        len(st.session_state.history)
    )

    st.metric(
        "Failed Requests",
        len(DEAD_LETTER_QUEUE)
    )

    st.metric(
        "Registered Tools",
        len(VALID_TOOLS)
    )