import streamlit as st

st.title("hello world")

st.write("simple test for streamlit")
st.header("this is a header")
st.subheader("this is a subheader")

# Création de bouton

if st.button("click me"):
    st.write("you clik me")
    st.balloons()

# creation de barre latéralle

st.sidebar.header("this is a sidebar")
button= st.sidebar.button(label="press me please")
if button:
    st.sidebar.write("hello freinds")
    st.balloons()
# creation de colonnes
col1, col2 = st.columns([3,1])
col1.header("column 1")
col1.write("column1")
col2.header("column 2")
col2.write("column2")

# add a selectbox to the sidebar
option=st.selectbox(
    'how would you be contacted?',
    ('email',' home phone','mobile phone')
    )
st.write('you selected', option)
