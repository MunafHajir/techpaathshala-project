import pandas as pd
from sklearn.neighbors import NearestNeighbors

movies = pd.read_csv("./movies.csv")
users = pd.read_csv("./users.csv")
ratings = pd.read_csv("./ratings.csv")


# print(movies.head())
# print(users.head())
# print(ratings.head())


data = pd.merge(movies, ratings, on="MovieID")


# print(data.head())

user_movie_matrix = data.pivot_table(index="UserID", columns="Title", values="Rating")

user_movie_matrix = user_movie_matrix.fillna(0)
user_movie_matrix.to_csv("output.csv")

model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(user_movie_matrix)


# model done



user_id = 1
# only 1st user data in 2d format
user_vector = user_movie_matrix.loc[user_id].values.reshape(1, -1)
print(user_vector)

distances, indices = model_knn.kneighbors(user_vector, n_neighbors=3)
similar_user_indices = indices.flatten()
print(similar_user_indices)

recommendations = []
for similar_user_index in similar_user_indices:
    if similar_user_index != user_id - 1:
        similar_user_id = user_movie_matrix.index[similar_user_index]
        similar_user_ratings = user_movie_matrix.loc[similar_user_id]
        recommendations.extend(similar_user_ratings[similar_user_ratings>=4].index.difference(user_movie_matrix.loc[user_id][user_movie_matrix.loc[user_id] > 0].index))
    
recommendations = list(set(recommendations))
print(f"Recommendations for User {user_id}: {recommendations}")









