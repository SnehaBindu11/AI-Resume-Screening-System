def calculate_skill_match(

    cleaned_resume,
    cleaned_job_description

):

    resume_words = set(cleaned_resume.split())

    job_words = set(cleaned_job_description.split())


    matched_skills = resume_words.intersection(job_words)

    if len(job_words) == 0:
        return 0, []

    score = (
        len(matched_skills) / len(job_words)
    ) * 100

    return round(score, 2), list(matched_skills)