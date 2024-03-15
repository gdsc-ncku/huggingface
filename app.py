import streamlit as st
from transformers import pipeline

st.write("Hello world")

# Load the model
generator = pipeline("text-generation", model="gpt2")  # you can use any model from the model hub

# prompt
prompt = st.text_input("Enter your prompt here")

# Generate the text
if st.button("Generate"):
    with st.spinner("Generating..."):
        result = generator(
            prompt,
            max_length=30,
            num_return_sequences=2,
        )
        st.write(result)
