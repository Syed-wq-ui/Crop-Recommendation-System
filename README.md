# 🌾 Khetify — AI Crop Recommendation System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4.2-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br/>

**An intelligent crop recommendation system powered by Machine Learning.**  
Enter your soil & weather data → Get the best crop suggestion instantly! 🚀

<br/>

[🌐 Live Demo](https://khetify.onrender.com) • [📊 Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset) • [🐛 Report Bug](https://github.com/Syed-wq-ui/Crop-Recommendation-System/issues)

<br/>

</div>

---

## 📸 Preview

> Enter N, P, K, Temperature, Humidity, pH, and Rainfall values → Get instant crop prediction with confidence score!

---

## ✨ Features

- 🤖 **Random Forest ML Model** — 200 trees, trained on 2200+ samples
- 📊 **Confidence Score** — Shows prediction probability percentage
- 🏆 **Top 3 Candidates** — Displays top 3 most suitable crops
- 🎨 **Beautiful UI** — Clean, responsive web interface
- ⚡ **Fast Predictions** — Results in milliseconds
- 📱 **Mobile Friendly** — Works on all screen sizes
- 🚀 **Live Deployed** — Accessible from anywhere in the world

---

## 🧠 How It Works

```
Soil & Weather Data Input
        ↓
   StandardScaler (Normalize)
        ↓
  Random Forest Classifier
   (200 Trees | sqrt features)
        ↓
   Label Decoder
        ↓
  🌾 Crop Prediction + Confidence %
```

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| **Test Accuracy** | ~99% |
| **Cross-Val Accuracy** | ~99% ± 0.002 |
| **Model Type** | Random Forest Classifier |
| **Trees** | 200 |
| **Training Samples** | 1760 |
| **Test Samples** | 440 |

---

## 🌱 Supported Crops (22 Classes)

| 🌾 Cereals | 🫘 Legumes | 🍎 Fruits | 🌿 Others |
|-----------|-----------|----------|---------|
| Rice | Chickpea | Mango | Cotton |
| Maize | Kidney Beans | Banana | Jute |
| | Pigeon Peas | Grapes | Coffee |
| | Mung Bean | Watermelon | |
| | Black Gram | Apple | |
| | Lentil | Pomegranate | |
| | | Papaya | |
| | | Coconut | |
| | | Orange | |
| | | Muskmelon | |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Backend** | Python, Flask |
| **ML Model** | Scikit-learn (Random Forest) |
| **Data Processing** | Pandas, NumPy |
| **Model Serialization** | Pickle |
| **Deployment** | Render (Free Tier) |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```
Khetify/
│
├── 📄 app.py                    # Flask backend & API routes
├── 📄 requirements.txt          # Python dependencies
├── 📄 Procfile                  # Render deployment config
│
├── 🤖 crop_model.pkl            # Trained Random Forest model
├── ⚖️  crop_scaler.pkl           # Fitted StandardScaler
├── 🏷️  crop_label_encoder.pkl    # Label Encoder (number → crop name)
│
├── 📊 Crop_recommendation.csv   # Dataset (2200 samples, 7 features)
├── 📓 crop_recommendation.ipynb # Training notebook
│
└── 📁 templates/
    └── 🌐 index.html            # Frontend UI
```

---

## ⚙️ Input Features

| Feature | Description | Unit |
|---------|-------------|------|
| **N** | Nitrogen content in soil | kg/ha |
| **P** | Phosphorus content in soil | kg/ha |
| **K** | Potassium content in soil | kg/ha |
| **Temperature** | Average temperature | °C |
| **Humidity** | Relative humidity | % |
| **pH** | Soil pH value | 0-14 |
| **Rainfall** | Annual rainfall | mm |

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/Syed-wq-ui/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```

**2. Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the app**
```bash
python app.py
```

**5. Open in browser**
```
http://127.0.0.1:5000
```

---

## 🌐 API Usage

**Endpoint:** `POST /predict`

**Request:**
```json
{
  "N": 117,
  "P": 32,
  "K": 34,
  "temperature": 26.27,
  "humidity": 52.12,
  "ph": 6.75,
  "rainfall": 127.17
}
```

**Response:**
```json
{
  "success": true,
  "crop": "rice",
  "emoji": "🌾",
  "confidence": 98.5,
  "top3": [
    { "crop": "rice",   "probability": 98.5 },
    { "crop": "maize",  "probability": 1.0  },
    { "crop": "jute",   "probability": 0.5  }
  ]
}
```

---

## 📈 Feature Importance

```
rainfall     | ████████████████████████████████████    0.28
humidity     | ████████████████████████████           0.22
K            | ████████████████████                   0.15
temperature  | ████████████████                       0.13
ph           | ████████████                           0.10
P            | ████████                               0.07
N            | █████                                  0.05
```

---

## 👨‍💻 Author

**Mohammad Farooque Ahmed**

[![GitHub](https://img.shields.io/badge/GitHub-Syed--wq--ui-181717?style=for-the-badge&logo=github)](https://github.com/Syed-wq-ui)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use it for your projects!

---

<div align="center">

Made with ❤️ and 🌾 by **Farooque**

⭐ **Star this repo if you found it useful!** ⭐

</div>