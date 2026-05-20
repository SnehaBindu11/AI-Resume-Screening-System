from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(vectors):

    similarity_score = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    similarity_percentage = similarity_score * 100

    return similarity_percentage