from sklearn.metrics.pairwise import cosine_similarity



def cosine_similarity_score(vec1, vec2):

    similarity = cosine_similarity(
        [vec1],
        [vec2]
    )

    return float(similarity[0][0])