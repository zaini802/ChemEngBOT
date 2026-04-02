import streamlit as st
import math

st.set_page_config(page_title="ChemEngBot", page_icon="🧪", layout="wide", initial_sidebar_state="expanded")

class ChemEngBot:
    def calculate_reynolds(self, rho, v, d, mu):
        return (rho * v * d) / mu
    
    def explain_concept(self, text):
        explanations = {
            'distillation': "Distillation is a separation process...",
            'heat exchanger': "Heat exchanger transfers heat between fluids...",
            'reactor': "Chemical reactor where reactions occur...",
            'pump': "Pump moves fluids...",
            'valve': "Valve controls flow...",
            'npsh': "NPSH prevents cavitation...",
            'cavitation': "Cavitation damages equipment...",
            'fouling': "Fouling reduces heat transfer..."
        }
        return explanations.get(text.lower(), "Ask about distillation, heat exchanger etc.")

bot = ChemEngBot()

# CSS FIXED - tested
st.markdown("""
<style>
/* Dark theme */
.stApp {background: linear-gradient(135deg, #16213e, #0f0f23); }

/* Sidebar WHITE text */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    color: white !important; font-size: 16px !important; font-weight: bold !important; }

section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2 {color: cyan !important; }

/* Main text WHITE */
.block-container h1, .block-container h2, .block-container p, .block-container li {color: white !important; }

/* Results BLACK text */
.stSuccess, .stInfo {color: black !important; }

/* Metrics CYAN */
[data-testid="metric-value"] {color: cyan !important; font-size: 3rem !important; }
[data-testid="metric-label"] {color: white !important; }

/* Avatar */
.header-avatar img {width: 60px; height: 60px; border-radius: 50%; border: 3px solid cyan; position: fixed; top: 20px; right: 20px; z-index: 1000; }
</style>
<div class="header-avatar">
    <img src="images/avatar.jpg" alt="Avatar">
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🧪 Navigation")
page = st.sidebar.radio("", ["Home", "Reynolds", "Heat Transfer", "Pressure Drop", "NTU", "Formulas", "Concepts"])

st.markdown("# 🧪 ChemEngBot")

if page == "Home":
    st.markdown("### Welcome!")
    st.markdown("Select sidebar option 👈")

elif page == "Reynolds":
    st.markdown("### Reynolds Number")
    col1, col2 = st.columns(2)
    rho = col1.number_input("ρ", 100.0)
    v = col1.number_input("v", 2.0)
    d = col2.number_input("d", 0.1)
    mu = col2.number_input("μ", 0.001)
    if st.button("Calculate"):
        Re = bot.calculate_reynolds(rho, v, d, mu)
        st.success(f"**Re = {Re:.0f}**")
        flow = "Laminar" if Re < 2300 else "Turbulent"
        st.info(f"Flow: **{flow}**")

# Add other pages similarly...

st.markdown("---")
st.markdown("**Zunair Shahzad | ChemEngBot**")
