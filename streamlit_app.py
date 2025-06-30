from openai import OpenAI
import streamlit as st

user = OpenAI(api_key="sk-")
gptmodel = "gpt-3.5-turbo"
userrole = "user"

pre_promt = "Teach me the following concept:"
reaspons = ""

st.title("PrefessorGPT App")
st.divider()
prompt = st.text_input("What do you want to learn?")
gptbutton = st.button("Teach Me")
st.caption("ProfessorGPT will Work When you press the button.")
st.divider


