import pandas as pd
import requests
import streamlit  as st
import pickle


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=b4a5cf9338c2f7271ab7a62a62cf0f84&language=en-US'.format(
            movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select one of your favourite movie",
    movies['title'].values)

if st.button('Recommend'):
    name, posters = recommend(selected_movie_name)

    num_columns = 3  # You can adjust the number of columns as per your preference
    columns = st.columns(num_columns)

    for i in range(len(name)):
        with columns[i % num_columns]:
            with st.expander(name[i]):
                st.image(posters[i])