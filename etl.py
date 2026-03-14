import streamlit as st
import pandas as pd

data ={
    "TASK":["EXTRACT","TRANSFORM","LOAD"],
    "STATUS":['COMPLETED','INPROGREE','PENDING']
}

df = pd.DataFrame(data)
st.title('ETL')
st.write(df)