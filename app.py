import streamlit as st
from openai import OpenAI
import os

# OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

st.set_page_config(page_title="QuadraMind AI", page_icon="🤖")

st.title(" QuadraMind AI ")
st.write("Ask me anything!")

# Chat history store
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your question here..."):

    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    response = client.chat.completions.create(
        model="meta-llama/llama-3-8b-instruct",
        messages=st.session_state.messages
    )

    answer = response.choices[0].message.content

    # Save AI message
    st.session_state.messages.append({"role": "assistant", "content": answer})

    with st.chat_message("assistant"):
        st.markdown(answer)
