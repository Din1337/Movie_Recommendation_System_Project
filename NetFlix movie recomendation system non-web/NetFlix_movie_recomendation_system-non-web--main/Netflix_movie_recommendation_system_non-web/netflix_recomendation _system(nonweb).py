# -*- coding: utf-8 -*-
"""
Movie Recommendation System
"""

# Import necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the movie dataset
movies = pd.read_csv(r"E:\movie_recommendation_system_project\NetFlix movie recomendation system non-web\NetFlix_movie_recomendation_system-non-web--main\Netflix_movie_recommendation_system_non-web\dataset_used\dataset.csv")

# Data exploration
print("Dataset description:")
print(movies.describe())
print("\nNull values count:")
print(movies.isnull().sum())
print("\nDataset columns:")
print(movies.columns)

print("\n" + "-" * 80 + "\n")

# Feature selection
movies = movies[['id', 'title', 'overview', 'genre']]
movies['tags'] = movies['overview'] + movies['genre']
newdata = movies.drop(columns=['overview', 'genre'])

print("-------------------------------MOVIE RECOMMENDATION SYSTEM-------------------------------")
print("\n")

# Text vectorization using CountVectorizer
cv = CountVectorizer(max_features=10000, stop_words='english')
vector = cv.fit_transform(newdata['tags'].values.astype('U')).toarray()
print("Vectorized data shape:", vector.shape)

print("\n" + "-" * 80 + "\n")

# Calculate cosine similarity between movie vectors
similarity = cosine_similarity(vector)

# Movie recommendation function
def recommand(movies):
    """
    Recommends similar movies based on the input movie title.
    
    Args:
        movies (str): The title of the movie to find recommendations for.
        
    Returns:
        list: A list of recommended movie titles, or None if no recommendations are found.
    """
    index = newdata[newdata['title'] == movies].index
    if not index.empty:
        index = index[0]
        if index < len(similarity):
            distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
            recommended_movies = [newdata.iloc[i[0]].title for i in distance[1:6]]  # Exclude the input movie
            return recommended_movies
    return None

# Function to list a sample of movie titles for testing
def list_random_movie_names(n=20):
    """
    Returns a random list of movie titles from the dataset.
    
    Args:
        n (int): The number of movie titles to return (default is 20).
        
    Returns:
        list: A random list of movie titles.
    """
    return newdata['title'].sample(n=n).tolist()

# Testing the recommendation system
print("Total of 10000 movie titles are here! For testing, 20 random movies are listed below:")
print("-" * 80)
random_movie_names = list_random_movie_names()
for name in random_movie_names:
    print("- " + name)

print("-" * 80)
user_input = input("Which movie would you like to watch? ")

recommended_movies = recommand(user_input)

if recommended_movies:
    print("You might also like these movies:")
    print("-" * 80)
    for movie in recommended_movies:
        print("- " + movie.upper())
else:
    print("Sorry, no recommendations found.")

print("-" * 80)
print("------------------------------------------------------------------------------------")
