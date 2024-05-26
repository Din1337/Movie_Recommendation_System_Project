Movie Recommendation System Documentation

1. Overview
⏩The Movie Recommendation System is designed to offer personalized movie recommendations based on user input. It leverages a dataset that includes movie details such as titles, overviews, and genres.

2. Dependencies
This system relies on the following libraries:

⏩Pandas: Used for data manipulation and analysis.
⏩Scikit-learn: Utilized for text vectorization and cosine similarity computation.

3. Functionality
⏩Data Loading: Loads the movie dataset from a CSV file.
⏩Data Exploration: Provides summary statistics, identifies missing values, and displays dataset columns.
⏩Feature Selection: Chooses relevant features (id, title, overview, genre) and combines them into a single 'tags' feature.
⏩Text Vectorization: Converts textual data into numerical vectors using CountVectorizer.
⏩Cosine Similarity: Calculates cosine similarity between vectorized text data to assess movie similarity.
⏩Recommendation: Suggests similar movies based on user input by utilizing cosine similarity scores.

4. Usage
⏩Load Data: Use the load_data function to load the movie dataset from a CSV file.
⏩Data Exploration: Utilize the data_exploration function to explore the dataset.
⏩Feature Selection: Apply the feature_selection function to choose and combine relevant features.
⏩Text Vectorization: Use the text_vectorization function to convert text data into vectors.
⏩Compute Similarity: Employ the compute_similarity function to calculate cosine similarity between vectors.
⏩Recommendation: Use the recommend_movies function to obtain movie recommendations based on user input.

5. Development Process
⏩Data Loading and Exploration: Load the dataset and explore its structure to understand its composition.
⏩Feature Selection: Choose relevant features and merge them into a single feature.
⏩Text Vectorization: Vectorize the text data using CountVectorizer.
⏩Cosine Similarity Calculation: Compute cosine similarity between vectors to determine movie similarity.
⏩Recommendation Generation: Input a movie title to receive personalized recommendations.

6. Future Enhancements
⏩Collaborative Filtering: Implement user-based or item-based collaborative filtering for more tailored recommendations.
⏩Additional Features: Integrate more features such as actors, directors, and release years to enhance recommendation accuracy.

7. Unit Testing and Integration
To ensure the robustness and accuracy of the recommendation system, various unit tests and integration tests are implemented using the unittest framework. These tests validate the functionality of different components of the system.

Example Unit Tests
⏩list_random_movie_names Function: Tests if the function returns the correct number of random movie names and ensures they exist in the dataset.
⏩recommand Function: Tests the recommendation functionality with valid and invalid movie titles.
⏩calculate_accuracy Function: Tests the accuracy calculation of the recommendation system based on genre similarity.

8. Model Accuracy
The accuracy of the recommendation model is calculated based on genre similarity. The calculate_accuracy function evaluates how well the recommended movies match the input movie's genre.

Example Calculation
⏩Correct Recommendations: Counts how many recommended movies share at least one genre with the input movie.
⏩Total Recommendations: The total number of recommended movies.

9. Contributors
⏩ Our fellow group teammates