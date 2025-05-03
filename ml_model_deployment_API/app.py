# app.py
from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Load data and similarity matrix
movies = joblib.load('movies.pkl')
similarity = joblib.load('similarity.pkl')

def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found."]
    
    index = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommendations = [movies.iloc[i[0]].title for i in sorted_movies]
    return recommendations

@app.route('/')
def home():
    return "Movie Recommendation API Running"

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    movie_name = data['movie']
    result = recommend(movie_name)
    return jsonify({'recommendations': result})

if __name__ == "__main__":
    app.run(debug=True)
