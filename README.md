# 🩺 Disease Predictor App

This is a **Flask-based web application** that predicts whether a patient has **Gestational Diabetes Mellitus (GDM)** or **Hypertensive Disorders of Pregnancy (HDP)** based on selected symptoms.  
It also **predicts patient vitals** (body temperature, blood pressure, heart rate, oxygen saturation) and **compares them with normal healthy ranges** for easy interpretation.

---

## 🚀 Features
- Predicts disease based on **user-selected symptoms**.
- Displays **predicted vital signs** (temperature, blood pressure, heart rate, oxygen levels).
- Compares patient vitals against **normal ranges** in a clean table.
- Fully responsive frontend using **HTML, CSS, JS**.
- Fast and lightweight **Flask backend** serving the ML model.
- Model trained on **custom symptom dataset**.

---

## 🛠 Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn
- **Model Storage**: joblib

---

## 📂 Project Structure
```
.
├── app.py               # Flask backend
├── model/
│   └── disease_predictor.pkl   # Trained ML model
├── preprocess.py         # Preprocessing & model training script
├── static/
│   ├── styles.css        # Frontend styling
│   └── script.js         # Frontend logic
├── templates/
│   └── index.html        # Main frontend page
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── dataset.csv           # Symptom-disease dataset
```

---

## ⚙️ Installation & Running Locally

1. **Clone the repository**  
```bash
git clone https://github.com/yourusername/disease-predictor-app.git
cd disease-predictor-app
```

2. **Create virtual environment (optional but recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the dependencies**  
```bash
pip install -r requirements.txt
```

4. **Run the application**  
```bash
python app.py
```

5. **Visit in Browser**  
Go to: `http://127.0.0.1:5000/`

---

## 🖥️ Demo Screenshots
| Symptom Selection | Prediction & Vitals |
| :---: | :---: |
| ![symptoms](screenshots/symptom-selection.png) | ![vitals](screenshots/predicted-vitals.png) |

*(Add screenshots if you want — optional but makes your repo look amazing!)*

---

## 📚 Future Improvements
- Add support for **more diseases**.
- Display **color-coded vitals** (green = normal, red = abnormal).
- Add **loading spinner** while prediction is processing.
- Integrate **user authentication** to save past predictions.

---

## 🙏 Acknowledgments
- Medical datasets inspiration from [Cleveland Clinic](https://my.clevelandclinic.org/) and [WHO resources](https://platform.who.int/).
- Special thanks to scikit-learn and Flask communities!

---

