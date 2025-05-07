import streamlit as st
from utils import extract_text_from_pdf, extract_skills, match_skills

st.set_page_config(page_title="CV Matchmaker", layout="centered")
st.title('🤖 CV Matchmaker')

st.markdown("**Align your CV with any Job Description in one click.**")

title = st.text_input("Job Title")
reqs = st.text_area("Paste Job Description")
cv = st.file_uploader("Upload your CV (PDF only)", type=['pdf'])

if st.button('Analyze'):
    if not (reqs and cv):
        st.warning("Please upload a CV and paste a job description.")
    else:
        with st.spinner("Analyzing..."):
            cv_text = extract_text_from_pdf(cv)
            jd_skills = extract_skills(reqs)
            matched, unmatched, suggestions = match_skills(cv_text, jd_skills)

            st.success("Analysis Complete!")

            st.subheader("✅ Matched Skills:")
            st.write(", ".join(matched) if matched else "None")

            st.subheader("❌ Unmatched Skills from JD:")
            st.write(", ".join(unmatched) if unmatched else "None")

            st.subheader("💡 Suggestions to Improve CV:")
            for sug in suggestions:
                st.markdown(f"- {sug}")