from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model/disease_predictor.pkl')

# List of all symptoms
symptoms = [
    'Frequent urination', 'Excessive thirst', 'Tiredness', 'Nausea',
    'Swelling feet', 'Sudden weight gain', 'Severe headache',
    'Blurred vision', 'Sudden nausea/vomiting',
    'Upper right abdominal pain', 'Shortness of breath'
]

@app.route('/')
def index():
    return render_template('index.html', symptoms=symptoms)

@app.route('/predict', methods=['POST'])
def predict():
    selected_symptoms = request.json.get('symptoms', [])
    
    # Create input vector
    input_vector = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
    
    # Predict disease
    prediction = model.predict([input_vector])[0]

    # Mock predicted vitals based on disease
    vitals = {}
    if prediction == 'GDM':
        vitals = {
            "Body Temperature (°F)": 98.6,
            "Blood Pressure (mmHg)": "120/80",
            "Heart Rate (bpm)": 85,
            "Oxygen Saturation (%)": 97
        }
    elif prediction == 'HDP':
        vitals = {
            "Body Temperature (°F)": 99.1,
            "Blood Pressure (mmHg)": "145/95",
            "Heart Rate (bpm)": 105,
            "Oxygen Saturation (%)": 94
        }

    # Normal healthy ranges
    normal_ranges = {
        "Body Temperature (°F)": "97-99",
        "Blood Pressure (mmHg)": "120/80",
        "Heart Rate (bpm)": "60-100",
        "Oxygen Saturation (%)": "95-100"
    }

    return jsonify({'prediction': prediction, 'vitals': vitals, 'normal_ranges': normal_ranges})

if __name__ == '__main__':
    app.run(debug=True)
