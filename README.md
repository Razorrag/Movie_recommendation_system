# movie-recommendation-system

This project was made by Anurag Singh and Prachi Agarwal this was made in order to learn more about classification task 

Overview

This project builds a content-based movie recommendation system using the TMDB 5000 Movies dataset. It suggests movies based on similarity calculated from movie tags derived from overviews, genres, keywords, cast, and crew.

Key Steps:

Data Preparation: Merge datasets, clean, and convert JSON-like columns into lists.

Feature Extraction: Use CountVectorizer to convert tags into numerical vectors.

Similarity Calculation: Compute cosine similarity between movies.

Recommendation: Function returns top 5 similar movies to a given title.

Model Saving: Store the DataFrame and similarity matrix using pickle.


Learnings:

Data merging and processing

Text vectorization techniques

Cosine similarity for recommendations

Model saving and deployment
