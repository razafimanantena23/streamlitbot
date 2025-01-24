import streamlit as st
from openai import OpenAI

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Set a default model and allow the user to select the model
model_options = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-instruct",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-0125"
]

# Create selectbox to choose the GPT model
selected_model = st.selectbox("Select GPT Model", model_options)

# Set default model if not already in session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = selected_model

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get the assistant's response
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model=selected_model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200,
        )

        # Get the response from the assistant
        assistant_message = response["choices"][0]["message"]["content"]
        st.markdown(assistant_message)
