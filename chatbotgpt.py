import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Dropdown for model selection
model_options = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-instruct",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-0125"
]
selected_model = st.selectbox("Choose a GPT model:", model_options)

# Store the selected model in session state
if "openai_model" not in st.session_state or st.session_state["openai_model"] != selected_model:
    st.session_state["openai_model"] = selected_model

# Slider for max_tokens selection
max_tokens = st.slider("Set maximum tokens for GPT response:", 0, 500, 200)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,  
            max_tokens=max_tokens, 
        )["choices"][0]["message"]["content"]
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
