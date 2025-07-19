def get_gemini_response(question):
  from dotenv import load_dotenv
  load_dotenv()
  import streamlit as st
  import google.genai as genai
  from model.prompt import retrievePrompt
  # creating client of genai which automatically fetches api key from dot-env file
  # GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
  client = genai.Client()
  prompt = retrievePrompt()
  response = client.models.generate_content(
    model="gemini-2.5-flash",contents=([prompt,question])
    )  
  print(response.text)
  return response.text.strip()


get_gemini_response("Show total revenue by gender")
