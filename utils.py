import fitz  # PyMuPDF
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    doc = nlp(text.lower())
    skills = set()
    for chunk in doc.noun_chunks:
        token = chunk.text.strip()
        if len(token.split()) < 5 and not token.startswith("•"):
            skills.add(token)
    return list(skills)

def match_skills(cv_text, jd_skills):
    matched = []
    unmatched = []
    suggestions = []

    cv_text_lower = cv_text.lower()
    for skill in jd_skills:
        if skill in cv_text_lower:
            matched.append(skill)
        else:
            unmatched.append(skill)
            suggestions.append(f"Consider adding experience or mention of **{skill}**.")

    return matched, unmatched, suggestions