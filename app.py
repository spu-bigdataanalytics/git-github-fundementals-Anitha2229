

import pickle
import streamlit as st
import requests
import pandas as pd


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movies_list:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names

st.title('Movie Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names= recommend(selected_movie_name)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
    with col2:
        st.text(recommended_movie_names[1])
    with col3:
        st.text(recommended_movie_names[2])
    with col4:
        st.text(recommended_movie_names[3])    
    with col5:
        st.text(recommended_movie_names[4]) 
    
