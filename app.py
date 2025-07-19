import streamlit as st
import pandas as pd
from model.generateQuery import get_gemini_response
from sql.readQuery import read_sql_query
from static.sampleQuestions import sampleQuestions
from sql.showDB import showDB
st.set_page_config("LLM-SQL",page_icon=":gear:",layout="wide")
st.title("🕵️‍♂️ Natural Language to SQL Assistant")

col1, col2 = st.columns(2)
with col1:
   showDB()

with col2:
   selectedQuestion = st.selectbox("Sample Questions",sampleQuestions,index=None,placeholder="Choose a sample question")

   st.markdown("OR")

   customQuestion = st.text_input("Enter your question below")

   question = customQuestion if customQuestion else (selectedQuestion if selectedQuestion else None)

   if(st.button(":blue[Run Gemini]")):
      with st.spinner("Loading results...."):
         if (question) :
            st.code(question)
            sql_query = get_gemini_response(question)
            if(sql_query.strip().lower() == "The question is unrelated to the database." or sql_query.strip().lower() == "The requested data is not available in the current database schema."):
               st.warning(sql_query)
            else:
               cols,rows = read_sql_query(sql_query)
               if len(cols)==0 and rows[0].startswith("Error while querying"):
                  st.warning("The question is unrelated to the database.")
               elif not rows:
                  st.warning("Not found")
               else:
                  if len(cols) == 1:
                     if len(rows) == 1:
                        st.success(rows[0][0])
                     else:
                        for row in rows:
                           st.write(row[0])
                  else:
                     # multiple columns and rows
                     # st.write("rows:", rows)
                     # st.write("cols:", cols)
                     df = pd.DataFrame(rows,columns=cols)
                     st.dataframe(df)
                  
                  st.code(sql_query, language="sql")
         else:
            st.warning("Write or select question to run gemini!")


