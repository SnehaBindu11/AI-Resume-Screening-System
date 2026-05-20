from extractor import extract_text_from_pdf

resume_path = "resumes/sample_resume.pdf"

resume_text = extract_text_from_pdf(resume_path)

print(resume_text)