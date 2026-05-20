def find_missing_keywords(

    vectorizer,
    cleaned_resume,
    cleaned_job_description

):

    resume_words = set(cleaned_resume.split())

    job_words = set(cleaned_job_description.split())

    missing_keywords = []

    for word in job_words:

        if word not in resume_words and len(word) > 2:

            missing_keywords.append(word)

    return sorted(missing_keywords)