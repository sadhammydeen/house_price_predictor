import pickle
from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Final_Project.csv"
MODEL_PATH = BASE_DIR / "regression_model.pkl"


@st.cache_data(show_spinner=False)
def load_dataset() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


@st.cache_resource(show_spinner=False)
def load_model():
    with MODEL_PATH.open('rb') as pickle_in:
        return pickle.load(pickle_in)


df = load_dataset()
reg = load_model()


def predict_price(area_sqft: float, floor_no: float, bedroom: float) -> float:
    x = np.zeros(7)
    x[0] = area_sqft
    x[1] = floor_no
    x[2] = bedroom
    return float(reg.predict([x])[0])


def run_ml_app() -> None:
    st.markdown("<h2 id='prediction-lab' class='page-title'>Prediction lab</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p class='page-subtitle'>Assemble property parameters, stress-test scenarios, and benchmark valuations against localized medians.</p>",
        unsafe_allow_html=True,
    )

    with st.form("prediction-form"):
        st.markdown("#### Scenario builder")
        col1, col2 = st.columns(2, gap="large")
        with col1:
            location = st.selectbox('Select location', sorted(df['Region'].unique()))
            area_sqft = st.slider("Total area (SqFt)", 500, int(df['Area_SqFt'].max()), step=100, value=int(df['Area_SqFt'].median()))
            floor_no = st.selectbox("Floor number", sorted(df['Floor_No'].unique()))
        with col2:
            bathroom = st.selectbox("Bathrooms", sorted(df['Bathroom'].unique()))
            bedroom = st.selectbox("Bedrooms", sorted(df['Bedroom'].unique()))
            property_age = st.selectbox('Property age', df['Property_Age'].sort_values().unique())
        st.markdown(
            "<span class='form-hint'>The baseline model currently uses area, floor, and bedroom features—additional selections contextualize the recommendation.</span>",
            unsafe_allow_html=True,
        )
        submitted = st.form_submit_button("Estimate price")

    if submitted:
        prediction = predict_price(area_sqft, float(floor_no), float(bedroom))
        region_median = df.loc[df['Region'] == location, 'Price_Lakh'].median()
        st.markdown(
            f"""
            <div class="neobrutalist-card result-card">
                <h3>Estimated market value</h3>
                <p class="price-highlight">{prediction:,.2f} Lakh</p>
                <p class="result-footnote">Regional median for {location}: {region_median:,.0f} Lakh</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="neobrutalist-card insight-card">
                <h3>Interpretation cues</h3>
                <ul>
                    <li>Use ready-to-move inventory as an anchor when negotiating premium corridors.</li>
                    <li>Compare with Data Analysis plots to validate outlier valuations.</li>
                    <li>Retune the workflow with fresh training data to incorporate additional features.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="neobrutalist-card insight-card">
                <h3>Build your first scenario</h3>
                <ul>
                    <li>Pick a locality to surface contextual medians.</li>
                    <li>Adjust square footage to watch the non-linear shifts.</li>
                    <li>Hit <strong>Estimate price</strong> to reveal the valuation panel.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        "<p class='stat-note'>Model version: Polynomial regression baseline (scikit-learn).</p>",
        unsafe_allow_html=True,
    )


if __name__ == '__main__':
    run_ml_app()