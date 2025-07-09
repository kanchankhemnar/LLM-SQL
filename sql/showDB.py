import streamlit as st
import pandas as pd
from sql.readQuery import read_sql_query
def showDB (toggle):
  st.session_state.show_db = toggle

  if st.session_state.show_db:
    columns, rows = read_sql_query("SELECT * FROM STUDENTS")
    if rows:
        df = pd.DataFrame(rows, columns=columns)
        st.dataframe(df)
    else:
        st.warning("No data found.")