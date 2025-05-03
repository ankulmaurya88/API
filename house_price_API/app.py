# app.py
from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the saved model
model = joblib.load('house_price_model.pkl')

@app.route('/')
def home():
    return "🏠 House Price Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        area = data.get('area')
        if area is None:
            return jsonify({"error": "Missing 'area' in request"}), 400
        
        prediction = model.predict([[area]])[0]
        return jsonify({"predicted_price": prediction})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
