import streamlit as st
import pandas as pd
from sql.readQuery import read_sql_query
def showDB ():
    columns, rows = read_sql_query("SELECT * FROM CUSTOMERS")
    if rows:
        df = pd.DataFrame(rows, columns=columns)
        st.write(":blue[CUSTOMERS]")
        st.dataframe(df)

    columns, rows = read_sql_query("SELECT * FROM PRODUCTS")
    if rows:
        df = pd.DataFrame(rows, columns=columns)
        st.write(":blue[PRODUCTS]")
        st.dataframe(df)

    columns, rows = read_sql_query("SELECT * FROM ORDERS")
    if rows:
        df = pd.DataFrame(rows, columns=columns)
        st.write(":blue[ORDERS]")
        st.dataframe(df)
    else:
        st.warning("No data found.")
