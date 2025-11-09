from pathlib import Path
import pandas as pd
from PIL import Image
import streamlit as st

from ml_app import run_ml_app
from eda_app import run_eda_app

st.set_page_config(page_title="Real Estate Price Lab", page_icon="🏙️", layout="wide")

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "IMG"
DATA_PATH = BASE_DIR / "Final_Project.csv"

NEOBRUTALIST_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

:root {
	--accent: #ff885b;
	--accent-dark: #ff5c2b;
	--bg: #f4f2eb;
	--ink: #111111;
	--muted: #585858;
	--surface: #fffdf6;
	--shadow: 8px 8px 0 rgba(17, 17, 17, 0.85);
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewContainer"] section {
	background-color: var(--bg);
	color: var(--ink);
	font-family: 'Space Grotesk', sans-serif;
}

h1, h2, h3, h4, h5, h6 {
	font-weight: 700;
	letter-spacing: 0.03em;
}

[data-testid="stSidebar"] {
	background: #ffe5d1;
	border-right: 4px solid var(--ink);
	box-shadow: 6px 0 0 rgba(17, 17, 17, 0.85);
}

[data-testid="stSidebar"] > div:first-child {
	padding: 2.5rem 1.5rem;
}

.sidebar-logo {
	font-size: 2.3rem;
	margin-bottom: 1.5rem;
	display: inline-block;
}

.sidebar-caption {
	margin-top: 2rem;
	font-size: 0.85rem;
	text-transform: uppercase;
	letter-spacing: 0.08em;
	color: var(--muted);
}

.page-title {
	font-size: clamp(2.4rem, 4vw, 3.2rem);
	text-transform: uppercase;
	margin-bottom: 0.3rem;
}

.page-subtitle {
	max-width: 760px;
	font-size: 1.1rem;
	color: var(--muted);
	margin-bottom: 2.2rem;
}

.neobrutalist-card {
	background: var(--surface);
	border: 4px solid var(--ink);
	box-shadow: var(--shadow);
	border-radius: 20px;
	padding: 2.4rem 2rem;
	margin-bottom: 2rem;
	text-align: left;
}

.hero-card {
	background: linear-gradient(135deg, #fffdf6 0%, #ffe5d1 80%);
}

.hero-card h2 {
	font-size: 2rem;
	margin-top: 0.5rem;
}

.badge {
	display: inline-block;
	background: var(--accent);
	color: var(--ink);
	padding: 0.35rem 1rem;
	border: 3px solid var(--ink);
	border-radius: 999px;
	box-shadow: 4px 4px 0 rgba(17, 17, 17, 0.85);
	font-weight: 600;
	text-transform: uppercase;
	font-size: 0.8rem;
}

.hero-list {
	margin-top: 1.5rem;
	padding-left: 1.2rem;
	list-style: square;
}

.hero-list li {
	margin-bottom: 0.45rem;
	font-weight: 500;
}

.steps-list {
	margin-top: 1rem;
	padding-left: 1.2rem;
}

.steps-list li {
	margin-bottom: 0.6rem;
}

.accent-card {
	background: var(--accent);
	color: var(--ink);
}

.accent-card h3,
.accent-card p,
.accent-card li {
	color: var(--ink);
}

.accent-link {
	display: inline-block;
	margin-top: 1.2rem;
	padding: 0.6rem 1.2rem;
	border: 3px solid var(--ink);
	background: #ffffff;
	color: var(--ink);
	text-decoration: none;
	font-weight: 600;
	box-shadow: 6px 6px 0 rgba(17, 17, 17, 0.85);
	cursor: pointer;
}

.accent-link:hover {
	background: var(--accent-dark);
	color: var(--ink);
}

button.accent-link {
	width: auto;
	font-family: inherit;
}

.social-grid {
	display: grid;
	grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
	gap: 1rem;
	margin-top: 1.5rem;
}

.social-grid a {
	display: block;
	padding: 0.85rem 1rem;
	border: 3px solid var(--ink);
	background: #ffffff;
	text-decoration: none;
	font-weight: 600;
	color: var(--ink);
	box-shadow: 5px 5px 0 rgba(17, 17, 17, 0.85);
	text-transform: uppercase;
	text-align: left;
}

.social-grid a:hover {
	background: var(--accent);
}

.map-card {
	padding: 0;
	overflow: hidden;
}

.map-card iframe {
	border: none;
	width: 100%;
}

.info-card ol {
	margin-bottom: 0;
}

.result-card {
	text-align: left;
	background: linear-gradient(135deg, #ffffff 0%, #ffe5d1 95%);
}

.price-highlight {
	font-size: clamp(2.4rem, 4vw, 3rem);
	font-weight: 700;
	margin: 1rem 0;
}

.result-footnote {
	font-size: 0.85rem;
	color: var(--muted);
}

.stat-note {
	display: block;
	margin-top: 0.6rem;
	font-size: 0.9rem;
	color: var(--muted);
}

.about-list {
	margin-top: 1rem;
	padding-left: 1.2rem;
}

.about-list li {
	margin-bottom: 0.5rem;
}

[data-testid="stMetricValue"] {
	font-weight: 700;
	color: var(--ink) !important;
}

[data-testid="metric-container"] {
	background: var(--surface);
	border: 4px solid var(--ink);
	border-radius: 18px;
	padding: 1.2rem;
	box-shadow: 6px 6px 0 rgba(17, 17, 17, 0.85);
	text-align: left;
	align-items: flex-start;
}

[data-testid="metric-container"] * {
	color: var(--ink) !important;
}

[data-testid="stMetricLabel"],
[data-testid="stMetricDelta"] {
	color: var(--ink) !important;
}

[data-testid="stMetricDelta"] svg {
	fill: var(--ink) !important;
}

label,
.stRadio label,
.stSelectbox label,
.stSlider label,
.stNumberInput label,
.stTextInput label,
.stMultiSelect label {
	color: var(--ink) !important;
	font-weight: 600;
}

[data-testid="stSidebar"] * {
	color: var(--ink) !important;
}

[data-baseweb="select"] * {
	color: var(--ink) !important;
}

.stSlider [data-testid="stTickBarLabel"] {
	color: var(--ink) !important;
}

.stSlider [data-testid="stTickBarMinLabel"],
.stSlider [data-testid="stTickBarMaxLabel"],
.stSlider [data-testid="stTickBarValue"] {
	color: var(--ink) !important;
}

.stSlider [role="slider"] {
	background: var(--accent) !important;
	border: 4px solid var(--ink) !important;
}

.stButton>button:disabled {
	background: #d8d5cc !important;
	color: rgba(17, 17, 17, 0.6) !important;
	box-shadow: 4px 4px 0 rgba(17, 17, 17, 0.35) !important;
}

[data-testid="stForm"] {
	background: var(--surface);
	border: 4px solid var(--ink);
	border-radius: 20px;
	padding: 2rem;
	box-shadow: var(--shadow);
}

.form-hint {
	display: block;
	margin-top: 1rem;
	font-size: 0.85rem;
	color: var(--muted);
}

.insight-card {
	background: #e6f0ff;
}

.insight-card h3 {
	margin-bottom: 0.8rem;
}

.insight-card ul {
	padding-left: 1.2rem;
}

/* Controls */
.stButton>button {
	background: var(--accent);
	color: var(--ink);
	border: 4px solid var(--ink);
	border-radius: 14px;
	padding: 0.8rem 1.6rem;
	font-weight: 600;
	text-transform: uppercase;
	box-shadow: 6px 6px 0 rgba(17, 17, 17, 0.85);
	transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.stButton>button:hover {
	transform: translate(-3px, -3px);
	box-shadow: 10px 10px 0 rgba(17, 17, 17, 0.85);
}

.stButton>button:focus:not(:focus-visible) {
	border: 4px solid var(--ink);
}

.stSelectbox>div>div,
.stSlider>div>div,
.stTextInput>div>div>input,
.stNumberInput>div>div>input,
[data-baseweb="select"]>div {
	border: 4px solid var(--ink) !important;
	border-radius: 16px !important;
	background: #ffffff !important;
	box-shadow: 4px 4px 0 rgba(17, 17, 17, 0.6);
}

.stSlider [role="slider"] {
	background: var(--accent) !important;
	border: 4px solid var(--ink) !important;
}

[data-testid="stDataFrame"],
[data-testid="stImage"] {
	border: 4px solid var(--ink);
	border-radius: 18px;
	padding: 0.6rem;
	box-shadow: 6px 6px 0 rgba(17, 17, 17, 0.85);
	background: #ffffff;
}

.stMarkdown a {
	color: var(--accent-dark);
	font-weight: 600;
}
</style>
"""

SOCIAL_LINKS = {
	"LinkedIn": "https://www.linkedin.com/in/hallishanu",
	"GitHub": "https://github.com/shanuhalli",
	"Email": "mailto:shanuhalli@gmail.com",
	"WhatsApp": "https://api.whatsapp.com/send/?phone=%2B919860934650&text&type=phone_number&app_absent=0",
}


def inject_custom_css() -> None:
	st.markdown(NEOBRUTALIST_CSS, unsafe_allow_html=True)
	st.markdown("""
		<script>
		const predictBtn = document.getElementById('prediction-btn');
		if (predictBtn) {
			predictBtn.addEventListener('click', function() {
				const radios = document.querySelectorAll('[role="radiogroup"] input');
				for (let radio of radios) {
					if (radio.value === "Prediction") {
						radio.click();
						break;
					}
				}
			});
		}
		</script>
	""", unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def load_dataset() -> pd.DataFrame:
	return pd.read_csv(DATA_PATH)


def render_home(df: pd.DataFrame) -> None:
	st.markdown("<h1 class='page-title'>Real Estate Price Lab</h1>", unsafe_allow_html=True)
	st.markdown(
		"<p class='page-subtitle'>A neo-brutalist command center fusing exploratory insights with predictive intelligence for Mumbai's property market.</p>",
		unsafe_allow_html=True,
	)

	hero_cols = st.columns([3, 2], gap="large")
	with hero_cols[0]:
		st.markdown(
			"""
			<div class="neobrutalist-card hero-card">
				<h2>Smarter investing starts here</h2>
				<p>Scan supply-demand signals, benchmark price corridors, and battle-test what-if scenarios with deliberate friction and bold clarity.</p>
				<ul class="hero-list">
					<li>Rapid exploratory narratives with curated datasets</li>
					<li>Scenario-based valuations powered by polynomial regression</li>
					<li>Purposefully vivid UI for uncompromising focus</li>
				</ul>
			</div>
			""",
			unsafe_allow_html=True,
		)
	with hero_cols[1]:
		hero_image = Image.open(IMG_DIR / "Realty_Growth.jpg")
		st.image(hero_image, caption="Mumbai skyline momentum", use_container_width=True)

	metric_cols = st.columns(3, gap="large")
	metric_cols[0].metric("Listings analyzed", f"{df.shape[0]:,}")
	metric_cols[1].metric("Median price (Lakh)", f"{df['Price_Lakh'].median():,.0f}")
	metric_cols[2].metric("Median area (SqFt)", f"{df['Area_SqFt'].median():,.0f}")

	info_cols = st.columns([2, 1], gap="large")
	with info_cols[0]:
		st.markdown(
			"""
			<div class="neobrutalist-card info-card">
				<h3>Choose your journey</h3>
				<p>Move between analytical and predictive views to form a conviction-backed perspective on Mumbai real estate.</p>
				<ol class="steps-list">
					<li>Open <strong>Data Analysis</strong> for macro and micro signals.</li>
					<li>Launch <strong>Prediction</strong> for scenario testing.</li>
					<li>Review <strong>About</strong> for deployment notes and contact.</li>
				</ol>
			</div>
			""",
			unsafe_allow_html=True,
		)
	with info_cols[1]:
		st.markdown(
			"""
			<div class="neobrutalist-card accent-card">
				<h3>Quick glance</h3>
				<p>Built by Sadham Mydeen to streamline negotiations with unapologetically bold visuals.</p>
			</div>
			""",
			unsafe_allow_html=True,
		)
		if st.button("Jump to prediction", key="prediction_button", type="primary"):
			st.session_state.page = "Prediction"
			st.rerun()


def render_about() -> None:
	st.markdown("<h2 class='page-title'>About the build</h2>", unsafe_allow_html=True)
	st.markdown(
		"""
		<div class="neobrutalist-card about-card">
			<h3>Designed for radical clarity</h3>
			<p>This deployment reimagines the Mumbai pricing workspace with a neo-brutalist visual language—strong contrasts, unapologetic borders, and legible hierarchy.</p>
			<ul class="about-list">
				<li>Web scraping pipeline capturing 99acres listings.</li>
				<li>Feature engineering and polynomial regression baseline modelling.</li>
				<li>Streamlit interface rebuilt with neo-brutalist principles.</li>
			</ul>
		</div>
		""",
		unsafe_allow_html=True,
	)

	path_to_html = IMG_DIR / "mumbai_property.html"
	if path_to_html.exists():
		st.markdown("<div class='neobrutalist-card map-card'>", unsafe_allow_html=True)
		with open(path_to_html, "r", encoding="utf-8") as html_file:
			html_data = html_file.read()
		st.components.v1.html(html_data, height=520, scrolling=True)
		st.markdown("</div>", unsafe_allow_html=True)


def main() -> None:
	inject_custom_css()
	df = load_dataset()

	menu = ["Home", "Data Analysis", "Prediction", "About"]
	if 'page' not in st.session_state:
		st.session_state.page = "Home"
	
	# Handle the prediction button click
	if st.session_state.get('prediction_button', False):
		st.session_state.page = "Prediction"
		st.session_state.prediction_button = False

	with st.sidebar:
		st.markdown("<span class='sidebar-logo'>🏙️</span>", unsafe_allow_html=True)
		choice = st.radio("Navigate", menu, index=menu.index(st.session_state.page), label_visibility="collapsed", key="navigation")
		st.session_state.page = choice
		st.markdown("<div class='sidebar-caption'>Sadham Mydeen • Mumbai Lifespaces</div>", unsafe_allow_html=True)

	if choice == "Home":
		render_home(df)
	elif choice == "Data Analysis":
		run_eda_app()
	elif choice == "Prediction":
		run_ml_app()
	else:
		render_about()


if __name__ == "__main__":
	main()