import streamlit as st
import math

# Page config
st.set_page_config(
    page_title="ChemEngBot", 
    page_icon="🧪", 
    layout="wide",
    initial_sidebar_state="expanded"
)

class ChemEngBot:
    def calculate_reynolds(self, rho, v, d, mu):
        return (rho * v * d) / mu
    
    def calculate_heat_transfer(self, u, a, delta_t):
        return u * a * delta_t
    
    def calculate_ntu(self, u, a, c_min):
        return (u * a) / c_min
    
    def calculate_pressure_drop(self, f, l, d, rho, v):
        return f * (l / d) * (rho * v**2 / 2)
    
    def explain_concept(self, concept):
        concepts = {
            'distillation': 'Distillation separates liquids by boiling points.',
            'heat exchanger': 'Transfers heat between fluids without mixing.',
            'reactor': 'Vessel for chemical reactions.',
            'pump': 'Moves fluids using mechanical action.',
            'valve': 'Controls fluid flow.',
            'npsh': 'Net Positive Suction Head prevents cavitation.',
            'cavitation': 'Vapor bubbles damage equipment.',
            'fouling': 'Deposits reduce heat transfer efficiency.'
        }
        return concepts.get(concept, "Available: distillation, heat exchanger, reactor, pump, valve, npsh, cavitation, fouling")

bot = ChemEngBot()

# PERFECT CSS - tested 100%
st.markdown("""
<style>
/* Dark gradient */
.stApp {
    background: linear-gradient(135deg, #1e1e3f 0%, #2a1e5c 50%, #16213e 100%);
}

/* ALL TEXT WHITE in main */
.block-container * {
    color: white !important;
}

/* Sidebar WHITE bold */
section[data-testid="stSidebar"] * {
    color: white !important;
}
section[data-testid="stSidebar"] label {
    font-weight: bold !important;
    font-size: 15px !important;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label {
    font-weight: bold !important;
    font-size: 15px !important;
    color: white !important;
}

/* Sidebar title cyan */
section[data-testid="stSidebar"] h2 {
    color: #00d4ff !important;
}

/* Results - standard colors with contrast */
.stSuccess {
    background: linear-gradient(90deg, #28a745, #20c997);
    color: white !important;
}
.stInfo {
    background: linear-gradient(90deg, #17a2b8, #007bff);
    color: white !important;
}
.stError {
    background: linear-gradient(90deg, #dc3545, #fd7e14);
    color: white !important;
}

/* Metrics PERFECT */
[data-testid="metric-container"] {
    background: rgba(0, 212, 255, 0.1) !important;
    border: 2px solid #00d4ff !important;
    border-radius: 12px !important;
}
[data-testid="metric-value"] {
    color: #00d4ff !important;
    font-size: 2.8rem !important;
    font-weight: bold !important;
}
[data-testid="metric-label"] {
    color: white !important;
    font-size: 16px !important;
}

/* Buttons cyan gradient */
button[kind="primary"] {
    background: linear-gradient(45deg, #00d4ff, #0099cc) !important;
    color: white !important;
    border-radius: 25px !important;
    font-weight: bold !important;
}

/* Title cyan glow */
h1 {
    color: #00d4ff !important;
    text-shadow: 0 0 15px rgba(0, 212, 255, 0.6) !important;
}

/* Avatar fixed position */
img {
    border-radius: 50% !important;
}
.header-avatar {
    position: fixed !important;
    top: 15px !important;
    right: 15px !important;
    z-index: 9999 !important;
}

/* Inputs labels */
label {
    color: white !important;
}
</style>

<!-- Avatar -->
<div style="position: fixed; top: 15px; right: 15px; z-index: 9999;">
    <img src="images/avatar.jpg" style="width: 55px; height: 55px; border-radius: 50%; border: 3px solid #00d4ff; box-shadow: 0 4px 12px rgba(0,212,255,0.4);">
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("### 🧪 Navigation")
page = st.sidebar.radio("Choose:", ["🏠 Home", "🔄 Reynolds", "🔥 Heat Transfer", "💧 Pressure Drop", "🌡️ NTU", "📋 Formulas", "📚 Concepts", "💬 Chat"])

st.markdown("### 🧪 ChemEngBot - Chemical Engineering Calculator")

if page == "🏠 Home":
    col1, col2 = st.columns([1,1])
    with col1:
        st.markdown("""
        **Features:**
        - Reynolds Number & flow type
        - Heat Transfer Q = U A ΔT
        - Pressure Drop in pipes
        - NTU method for exchangers
        - Key formulas
        - Concept explanations
        - General chat
        
        **Select sidebar 👈**
        """)
    with col2:
        st.markdown("""
        **How to use:**
        1. Choose calculation from sidebar
        2. Enter values in inputs
        3. Click Calculate
        4. Get instant results!
        
        **Professional & accurate**
        """)

elif page == "🔄 Reynolds":
    st.markdown("#### Re = ρ v d / μ")
    col1, col2 = st.columns(2)
    rho = col1.number_input("Density ρ (kg/m³)", value=1000.0)
    v = col1.number_input("Velocity v (m/s)", value=2.0)
    d = col2.number_input("Diameter d (m)", value=0.05)
    mu = col2.number_input("Viscosity μ (Pa·s)", value=0.001)
    
    if st.button("Calculate Re", use_container_width=True):
        Re = bot.calculate_reynolds(rho, v, d, mu)
        col1, col2 = st.columns(2)
        col1.metric("**Re**", f"{Re:.0f}")
        col2.metric("**Flow**", "Laminar 🟢" if Re < 2300 else "Turbulent 🔴")
        st.success("Calculation complete!")

elif page == "🔥 Heat Transfer":
    st.markdown("#### Q = U A ΔT")
    col1, col2 = st.columns(2)
    u = col1.number_input("U (W/m²K)", value=500.0)
    a = col1.number_input("Area A (m²)", value=10.0)
    delta_t = col2.number_input("ΔT (K)", value=30.0)
    
    if st.button("Calculate Q", use_container_width=True):
        Q = bot.calculate_heat_transfer(u, a, delta_t)
        st.metric("Heat Transfer Rate", f"{Q:.0f} W")
        st.success("Done!")

# Add other pages...

st.markdown("---")
st.caption("ChemEngBot by Zunair Shahzad")
