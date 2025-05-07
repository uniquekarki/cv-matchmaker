import streamlit as st

st.title('CV Matchmaker')

title = st.text_input("Job Title")
reqs = st.text_area("Job Description")
cv = st.file_uploader("Upload your CV")

if st.button('Analyze'):
    st.write('Well Done!')