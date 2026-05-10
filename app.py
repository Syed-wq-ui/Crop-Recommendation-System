from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load all pickle files
with open('crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('crop_scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('crop_label_encoder.pkl', 'rb') as f:
    le = pickle.load(f)

FEATURE_COLUMNS = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# Crop emoji mapping
CROP_EMOJI = {
    'rice': '🌾', 'maize': '🌽', 'chickpea': '🫘', 'kidneybeans': '🫘',
    'pigeonpeas': '🫘', 'mothbeans': '🫘', 'mungbean': '🫘', 'blackgram': '🫘',
    'lentil': '🫘', 'pomegranate': '🍎', 'banana': '🍌', 'mango': '🥭',
    'grapes': '🍇', 'watermelon': '🍉', 'muskmelon': '🍈', 'apple': '🍎',
    'orange': '🍊', 'papaya': '🍈', 'coconut': '🥥', 'cotton': '🌿',
    'jute': '🌿', 'coffee': '☕'
}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall']),
        ]

        sample        = np.array(features).reshape(1, -1)
        sample_scaled = scaler.transform(sample)
        pred_index    = model.predict(sample_scaled)[0]
        pred_proba    = model.predict_proba(sample_scaled)[0]
        confidence    = round(pred_proba.max() * 100, 2)
        crop_name     = le.inverse_transform([pred_index])[0]

        # Top 3
        top3_idx   = pred_proba.argsort()[::-1][:3]
        top3_crops = le.inverse_transform(top3_idx)
        top3 = [
            {'crop': c, 'probability': round(pred_proba[i] * 100, 2)}
            for c, i in zip(top3_crops, top3_idx)
        ]

        emoji = CROP_EMOJI.get(crop_name.lower(), '🌱')

        return jsonify({
            'success': True,
            'crop': crop_name,
            'emoji': emoji,
            'confidence': confidence,
            'top3': top3
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
