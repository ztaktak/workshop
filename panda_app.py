import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
# création des interfaces
st.title("bienvenue chez Test AI")
st.write("simple test for streamlit")
file = st.file_uploader('upload a csv file', type=['csv'])
question = st.text_input('how can i help you')

# creation de base de données depuis un fichier
if file is not None:
    df= pd.read_csv(file)
    st.write(df)

# Instantiate a LLM
llm = OpenAI(api_token="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")

if st.button('how can i help you') and file is not None:
    pandas_ai = PandasAI(llm, conversational=False)
    # ajouter un spinner 
    with st.spinner('thinking ...'):
        reponse = pandas_ai(df, prompt='question')
        st.write(reponse)
        st.write("done")
