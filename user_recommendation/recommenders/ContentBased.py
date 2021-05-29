import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


def contentBased(rs_df, bestSeller):
    count = CountVectorizer()
    count_matrix = count.fit_transform(rs_df['bag_of_words'])
    indices = pd.Series(rs_df.index)
    cosin_sim = cosine_similarity(count_matrix)
    recommender = recommendation(rs_df, bestSeller, cosin_sim, indices)
    return recommender


def bagofwords(rs_df):
    cols = ['FAMILLE', 'UNIVERS', 'MAILLE']
    rs_df['bag_of_words'] = rs_df[cols].apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
    rs_df = rs_df.drop(cols, axis=1)
    rs_df.set_index('LIBELLE', inplace=True)
    return rs_df


def recommendation(rs, bestSeller, cosin_sim, indices):
    recommended_product = []
    idx = indices[indices == bestSeller].index[0]
    score_series = pd.Series(cosin_sim[idx]).sort_values(ascending=False)
    top_10_indexes = list(score_series.iloc[1:11].index)

    for i in top_10_indexes:
        recommended_product.append(list(rs.index)[i])

    return recommended_product

def toString(recommendation, bestSeller):
    print("\n""------------------------------------------")
    print("Top 10 recommended products for you :""\n")
    for i in recommendation:
        print(i)
    print("\n""------------------------------------------""\n")
    print("This recommendation is based on your best buy""\n")
    for i in bestSeller:
        print(i)