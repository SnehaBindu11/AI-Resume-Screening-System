from extractor import extract_text_from_pdf
from preprocess import preprocess_text


resume_path = "resumes/sample_resume.pdf"

raw_text = extract_text_from_pdf(resume_path)

cleaned_text = preprocess_text(raw_text)

print(cleaned_text)