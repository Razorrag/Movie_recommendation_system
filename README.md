# movie-recommendation-system

This project was made by Anurag Singh and Prachi Agarwal this was made in order to learn more about classification task 

Overview

This project builds a content-based movie recommendation system using the TMDB 5000 Movies dataset. It suggests movies based on similarity calculated from movie tags derived from overviews, genres, keywords, cast, and crew.

Key Steps:

1)Data Preparation: Merge datasets, clean, and convert JSON-like columns into lists.

2)Feature Extraction: Use CountVectorizer to convert tags into numerical vectors.

3)Similarity Calculation: Compute cosine similarity between movies.

4)Recommendation: Function returns top 5 similar movies to a given title.

5)Model Saving: Store the DataFrame and similarity matrix using pickle.


Learnings:

1)Data merging and processing

2)Text vectorization techniques

3)Cosine similarity for recommendations

4)Model saving and deployment
