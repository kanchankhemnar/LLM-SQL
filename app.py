import streamlit as st
import pandas as pd
from model.generateQuery import get_gemini_response
from sql.readQuery import read_sql_query
from static.sampleQuestions import sampleQuestions
from sql.showDB import showDB
st.set_page_config("LLM-SQL",page_icon=":gear:")
st.title("🧠 Natural Language to SQL Assistant")

if "show_db" not in st.session_state:
   st.session_state.show_db = True

if st.button("📊 Show Database"):
   showDB(True)
   if(st.button("Hide Database")):
      showDB(False)

selectedQuestion = st.selectbox("Sample Questions",sampleQuestions,index=None,placeholder="Choose a sample question")

st.markdown("OR")

customQuestion = st.text_input("Enter your question below")

question = customQuestion if customQuestion else (selectedQuestion if selectedQuestion else None)

if(st.button(":blue[Run Gemini]")):
   if (question) :
      st.code(question)
      sql_query = get_gemini_response(question)
      cols,rows = read_sql_query(sql_query)
      if not rows:
         st.warning("Not found")
      else:
         if len(cols) == 1:
            if len(rows) == 1:
               # (['CE',])
               st.success(rows[0][0])
            else:
               for row in rows:
                  st.write(row[0])
         else:
            # multiple columns and rows
            df = pd.DataFrame(rows,columns=cols)
            st.dataframe(df)
         
         st.code(sql_query, language="sql")
   else:
      st.warning("Write or select question to run gemini!")


