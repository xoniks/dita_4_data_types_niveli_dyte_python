import pandas as pd

# from pathlib import Path

# p = Path(__file__)
# data_path = str(p.cwd())+'\data\\'

# file_input = data_path+'data_input.csv'

import streamlit as st

file_input = st.file_uploader('Please upload your file', type=['csv','txt'])    

# df= None

if file_input:
    df = pd.read_csv(file_input)
    df['domain'] = df['email'].apply(lambda x : x.split('@')[1])
    
if st.button('Print columns'):
    st.write(df['domain'])
    
@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

if st.button('Generate file '):
    csv = convert_df(df['domain'])
    st.download_button(
        label="Download data as CSV",   
        data=csv,
        file_name=st.text_input('Please enter file name:'),
        mime='text/csv',  
    )



# print(ser.apply(lambda x: x*2))