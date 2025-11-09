from pathlib import Path
import pandas as pd
from PIL import Image
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "IMG"
DATA_PATH = BASE_DIR / "Final_Project.csv"


@st.cache_data(show_spinner=False)
def _load_dataset() -> pd.DataFrame:
	return pd.read_csv(DATA_PATH)


def _chunk(items, size):
	for index in range(0, len(items), size):
		yield items[index:index + size]


def run_eda_app() -> None:
	st.markdown("<h2 class='page-title'>Data analysis studio</h2>", unsafe_allow_html=True)
	st.markdown(
		"<p class='page-subtitle'>Discover the structural patterns and outliers driving Mumbai's price dynamics before running prediction experiments.</p>",
		unsafe_allow_html=True,
	)

	df = _load_dataset()
	submenu = st.sidebar.radio(
		"Analysis lens",
		["Descriptive overview", "Visual gallery"],
		index=0,
		key="eda-lens",
	)

	metrics = st.columns(4, gap="large")
	metrics[0].metric("Median price", f"{df['Price_Lakh'].median():,.0f} Lakh")
	metrics[1].metric("Median area", f"{df['Area_SqFt'].median():,.0f} SqFt")
	metrics[2].metric("Ready-to-move", f"{(df['Availability'] == 'Ready To Move').mean() * 100:,.0f}%")
	metrics[3].metric("Median rate / SqFt", f"₹{df['Rate_SqFt'].median():,.0f}")

	if submenu == "Descriptive overview":
		preview_cols = st.columns([2, 1], gap="large")
		with preview_cols[0]:
			st.markdown("#### Dataset snapshot")
			st.dataframe(df.head(30), use_container_width=True)
		with preview_cols[1]:
			st.markdown("#### Feature glossary")
			st.markdown(
				"""
				- **Price_Lakh**: Target valuation in Indian Lakhs.
				- **Area_SqFt**: Super / carpet area normalized to square feet.
				- **Rate_SqFt**: Derived rate per square foot across listings.
				- **Availability**: Ready-to-move versus under-construction signals.
				- **Region**: Curated sub-markets across Mumbai, Navi Mumbai, and Thane.
				"""
			)

		st.markdown("#### Summary statistics")
		st.dataframe(df.describe().T, use_container_width=True)

		st.markdown("#### Dominant regions")
		top_regions = df["Region"].value_counts().head(12)
		st.bar_chart(top_regions)

	else:
		st.markdown("#### Visual gallery")
		plot_catalog = [
			("Real_Estate.jpg", "Market pulse overview", "A wide-angle look at the aggregated inventory landscape."),
			("Price_Range_Distribution.png", "Price range distribution", "Price density reveals asymmetric premium clusters."),
			("Property_Floor_Numbers_Bar.png", "Floor level vs price", "Higher floors command a notable premium in vertical micro-markets."),
			("BednBath_Price_Bar.png", "Bedrooms & bathrooms", "Bedroom-bathroom pairings that bend the price curve."),
			("Price_Age_Distribution.png", "Age vs price", "Legacy developments still dominate the luxury segment."),
			("SqFt_Area_Price_Scatter.png", "Area vs price scatter", "Non-linear pockets of value across square-footage bands."),
			("Central Mumbai.png", "Central Mumbai spotlight", "Premium cores with steep appreciation trajectories."),
			("South Mumbai.png", "South Mumbai spotlight", "Historic enclaves balancing heritage and demand."),
			("Thane.png", "Thane spotlight", "Satellite expansions pulling in mid-market budgets."),
		]

		for row in _chunk(plot_catalog, 3):
			cols = st.columns(len(row), gap="large")
			for col, (filename, title, caption) in zip(cols, row):
				with col:
					image = Image.open(IMG_DIR / filename)
					st.image(image, caption=title, use_column_width=True)
					st.markdown(f"<span class='stat-note'>{caption}</span>", unsafe_allow_html=True)