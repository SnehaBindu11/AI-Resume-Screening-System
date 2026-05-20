from extractor import extract_text_from_pdf
from preprocess import preprocess_text
from vectorizer import vectorize_documents


resume_path = "resumes/sample_resume.pdf"

raw_resume_text = extract_text_from_pdf(resume_path)

cleaned_resume = preprocess_text(raw_resume_text)


job_description = """
Looking for a Python developer with experience in
Machine Learning, SQL, NLP, TensorFlow, AWS,
Data Analysis, and Web Development.
"""

cleaned_job_description = preprocess_text(job_description)


vectors, vectorizer = vectorize_documents(
    cleaned_resume,
    cleaned_job_description
)

print(vectors.toarray())

print("\nFeature Names:\n")

print(vectorizer.get_feature_names_out())