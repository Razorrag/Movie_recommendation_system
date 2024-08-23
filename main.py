import streamlit as st
import pickle
import pandas as pd

# Load the preprocessed data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert the dictionary back to a DataFrame
movies = pd.DataFrame(movies_dict)

# Function to recommend movies
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
        return recommended_movies
    except IndexError:
        return ["Movie not found!"]

# Streamlit App UI
st.title("Movie Recommendation System")

# Dropdown menu for movie selection
movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

# Recommend button
if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    if recommendations[0] == "Movie not found!":
        st.error("Movie not found! Please try another title.")
    else:
        st.success("Recommended Movies:")
        for movie in recommendations:
            st.write(movie)
