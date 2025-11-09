# Real Estate Price Lab

Modern Streamlit workspace for analyzing and predicting property prices across the Mumbai metropolitan region. Inspired by a neo-brutalist design system, the app blends sharp visuals with focused workflows.

---

## ✨ Highlights
- Dual workflows: exploratory data analysis studio and interactive prediction lab
- Polynomial regression baseline trained on curated 99acres listings
- Bold UI with immediate insight cards, contextual medians, and curated visual gallery

---

## 🧠 Project Overview

| Area | Details |
| --- | --- |
| **Goal** | Provide a single interface to inspect market patterns and simulate property valuations |
| **Dataset** | Scraped 99acres Mumbai listings, cleaned and merged into `Final_Project.csv` |
| **Tech Stack** | Python, Pandas, Scikit-learn, Streamlit, Pillow |
| **Model** | Pipeline with polynomial feature expansion and linear regression |
| **Deployment** | Streamlit app designed with custom CSS and modern layout modules |

---

## 🗂️ Repository Structure

```
Project-Real-Estate-Price-Prediction/
├── Deployment/
│   ├── app.py               # Streamlit shell with neo-brutalist theme
│   ├── eda_app.py           # Data analysis studio module
│   ├── ml_app.py            # Prediction lab module
│   ├── regression_model.pkl # Serialized scikit-learn pipeline
│   └── IMG/                 # Visual assets and HTML map embed
├── Datasets/
│   └── Final_Project.csv    # Primary dataset
└── notebooks                # Jupyter notebooks for scraping, cleaning, analysis
```

---

## 🚀 Quick Start

### 1. Clone & set up environment
```bash
# clone the repository
git clone https://github.com/sadhammydeen/house_price_predictor.git
cd house_price_predictor

# create virtual environment (Python 3.9+ recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

> If you only plan to run the Streamlit app, use the trimmed requirements inside `Deployment/requirements.txt`.

### 3. Launch the Streamlit experience
```bash
cd Deployment
streamlit run app.py
```

Navigate to the URL printed in your terminal (default `http://localhost:8501`).

---

## 🧭 Using the App
- **Home**: Overview metrics, workflow guidance, and quick navigation links.
- **Data Analysis**: Explore descriptive statistics, top-region charts, and curated plot gallery.
- **Prediction**: Configure scenarios (location, area, floor, bedrooms, etc.) and run the polynomial regression estimator with contextual median pricing.
- **About**: Map overview plus contact links for Sadham Mydeen.

---

## 🔁 Retraining the Model
1. Extend or refresh `Final_Project.csv` inside `Deployment/`.
2. Update the notebooks in `Project-Real-Estate-Price-Prediction/notebooks/` to rebuild the feature pipeline.
3. Serialize the updated model to `Deployment/regression_model.pkl` (ensure scikit-learn version compatibility).
4. Restart the Streamlit app to pick up the new model.

---

