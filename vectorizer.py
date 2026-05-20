from sklearn.feature_extraction.text import TfidfVectorizer


def vectorize_documents(resume_text, job_description_text):

    vectorizer = TfidfVectorizer(

        ngram_range=(1, 2),
        stop_words='english'

    )

    vectors = vectorizer.fit_transform([

        resume_text,
        job_description_text

    ])

    return vectors, vectorizer