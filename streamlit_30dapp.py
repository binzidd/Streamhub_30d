import streamlit as st
st.write('Hello World!')


st.header('st.button')

if st.button('Say Hello'):
	st.write('Why hello there')

else: 
	st.write('Goodbye')

## add a sidebar 

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)