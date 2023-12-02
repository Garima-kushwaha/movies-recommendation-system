import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=a175c46aaeb966a9a8ca7c08a78bee6a&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return movies_list


movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movies Recommendation System')

selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values
)

if st.button('Show Recommendation'):

    col1, col2, col3, col4, col5 = st.columns(5)
    movies_list = recommend(selected_movie_name)
    for idx, i in enumerate(movies_list):
        recommended_movie_name = movies.iloc[i[0]].title
        recommended_movie_poster = fetch_poster(movies.iloc[i[0]].id)

        if idx % 5 == 0:
            with col1:
                st.subheader(recommended_movie_name)
                st.image(recommended_movie_poster)
        elif idx % 5 == 1:
            with col2:
                st.subheader(recommended_movie_name)
                st.image(recommended_movie_poster)
        elif idx % 5 == 2:
            with col3:
                st.subheader(recommended_movie_name)
                st.image(recommended_movie_poster)
        elif idx % 5 == 3:
            with col4:
                st.subheader(recommended_movie_name)
                st.image(recommended_movie_poster)
        elif idx % 5 == 4:
            with col5:
                st.subheader(recommended_movie_name)
                st.image(recommended_movie_poster)
