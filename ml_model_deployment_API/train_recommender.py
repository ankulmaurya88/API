# train_recommender.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

# Sample movie dataset
data = {
    'title': ['Inception', 'The Matrix', 'Interstellar', 'The Prestige', 'Memento'],
    'tags': [
        'sci-fi dream mind', 
        'sci-fi reality computer',
        'space time science',
        'magic trick rivalry',
        'memory loss puzzle'
    ]
}

df = pd.DataFrame(data)

# Text vectorization
cv = CountVectorizer()
vectors = cv.fit_transform(df['tags']).toarray()

# Compute similarity matrix
similarity = cosine_similarity(vectors)

# Save necessary files
joblib.dump(df, 'movies.pkl')
joblib.dump(similarity, 'similarity.pkl')
