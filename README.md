# Movie Recommendation System Documentation

## 1. Project Overview
![Project Overview]
The Movie Recommendation System is designed to offer personalized movie recommendations based on user input. It leverages a dataset that includes movie details such as titles, overviews, and genres.

## 2. Installation Instructions
![Installation Instructions]

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Din1337/Movie_Recommendation_System_Project
    cd movie_recommendation_system
    ```

2. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    **Pandas**: Used for data manipulation and analysis.
    **Scikit-learn**: Utilized for text vectorization and cosine similarity computation.
    ```

3. **Download the dataset:**
    Place the dataset file (`dataset.csv`) in the `dataset_used` directory.

## 3. Usage Guidelines
![Usage Guidelines]

1. **Run the recommendation system:**
    ```bash
    python main.py
    ```

2. **Interact with the system:**
    - The system will list 20 random movie titles from the dataset.
    - Input a movie title to get recommendations.

## 4. Contribution Guidelines
![Contribution Guidelines]

Contributions are welcome! Please follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**
    ```bash
    git checkout -b feature-branch
    ```
3. **Commit your changes:**
    ```bash
    git commit -m 'Add new feature'
    ```
4. **Push to the branch:**
    ```bash
    git push origin feature-branch
    ```
5. **Open a pull request.**

## 5. Functionality

- **Data Loading**: Loads the movie dataset from a CSV file.
- **Data Exploration**: Provides summary statistics, identifies missing values, and displays dataset columns.
- **Feature Selection**: Chooses relevant features (id, title, overview, genre) and combines them into a single 'tags' feature.
- **Text Vectorization**: Converts textual data into numerical vectors using `CountVectorizer`.
- **Cosine Similarity**: Calculates cosine similarity between vectorized text data to assess movie similarity.
- **Recommendation**: Suggests similar movies based on user input by utilizing cosine similarity scores.

## 6. Development Process

1. **Data Loading and Exploration**: Load the dataset and explore its structure to understand its composition.
2. **Feature Selection**: Choose relevant features and merge them into a single feature.
3. **Text Vectorization**: Vectorize the text data using `CountVectorizer`.
4. **Cosine Similarity Calculation**: Compute cosine similarity between vectors to determine movie similarity.
5. **Recommendation Generation**: Input a movie title to receive personalized recommendations.

## 7. Future Enhancements

- **Collaborative Filtering**: Implement user-based or item-based collaborative filtering for more tailored recommendations.
- **Additional Features**: Integrate more features such as actors, directors, and release years to enhance recommendation accuracy.

## 8. Unit Testing and Integration
To ensure the robustness and accuracy of the recommendation system, various unit tests and integration tests are implemented using the `unittest` framework. These tests validate the functionality of different components of the system.

### Example Unit Tests

- **list_random_movie_names Function**: Tests if the function returns the correct number of random movie names and ensures they exist in the dataset.
- **recommand Function**: Tests the recommendation functionality with valid and invalid movie titles.
- **calculate_accuracy Function**: Tests the accuracy calculation of the recommendation system based on genre similarity.

## 9. Model Accuracy

The accuracy of the recommendation model is calculated based on genre similarity. The `calculate_accuracy` function evaluates how well the recommended movies match the input movie's genre.

### Example Calculation

- **Correct Recommendations**: Counts how many recommended movies share at least one genre with the input movie.
- **Total Recommendations**: The total number of recommended movies.

## 10. Contributors

Our fellow group teammates.

