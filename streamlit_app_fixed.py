import streamlit as st
import math

# Set page configuration
st.set_page_config(page_title="ChemEngBot", page_icon="🧪", layout="wide", initial_sidebar_state="expanded")

class ChemEngBot:
    def __init__(self):
        self.name = "ChemEngBot"
    
    def calculate_reynolds(self, rho, v, d, mu):
        """Re = ρvd/μ"""
        return (rho * v * d) / mu
    
    def calculate_heat_transfer(self, u, a, delta_t):
        """Q = U A ΔT"""
        return u * a * delta_t
    
    def calculate_ntu(self, u, a, c_min):
        """NTU = UA/Cmin"""
        return (u * a) / c_min
    
    def calculate_pressure_drop(self, f, l, d, rho, v):
        """ΔP = f * (L/D) * (ρv²/2)"""
        return f * (l / d) * (rho * v**2 / 2)
    
    def explain_concept(self, text):
        explanations = {
            'distillation': "Distillation: A separation process that uses boiling point differences. Hot vapor rises, cool liquid falls. Used in refineries to separate crude oil into petrol, diesel, etc.",
            'heat exchanger': "Heat Exchanger: A device that transfers heat between two fluids without mixing them. Types include shell-and-tube, plate, and double-pipe.",
            'reactor': "Chemical Reactor: Vessel where chemical reactions occur. Types: CSTR (Continuous Stirred Tank), PFR (Plug Flow), and Batch Reactors.",
            'pump': "Pump: A device that moves fluids by mechanical action. Types: centrifugal, positive displacement, diaphragm pumps.",
            'valve': "Valve: Controls fluid flow. Types: gate, globe, ball, butterfly, check valves.",
            'npsh': "NPSH (Net Positive Suction Head): Minimum pressure required at pump suction to avoid cavitation. Critical for pump selection.",
            'cavitation': "Cavitation: Formation of vapor bubbles in liquid due to low pressure. Damages pumps and valves. Prevented by maintaining adequate NPSH.",
            'fouling': "Fouling: Deposit buildup on heat exchanger surfaces. Reduces efficiency. Prevented by cleaning and using fouling factors in design."
        }
        
        text_lower = text.lower()
        for key, value in explanations.items():
            if key in text_lower:
                return value
        
        return "I can explain: distillation, heat exchanger, reactor, pump, valve, NPSH, cavitation, fouling. Ask 'what is' followed by any of these terms!"

# Initialize the bot
bot = ChemEngBot()

# Perfect CSS - tested & working
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
}

/* All main text WHITE */
.main * {
    color: white !important;
}

.main p, .main h1, .main h2, .main h3, .main h4 {
    color: white !important;
}

/* Sidebar WHITE text */
[data-testid="stSidebar"] * {
    color: white !important;
}

.stSidebar label {
    font-weight: bold !important;
    font-size: 16px !important;
}

.stSidebar h1, .stSidebar h2 {
    color: #00ffff !important;
}

/* Results - black text on colored bg */
.stSuccess {
    background-color: #d4edda !important;
    color: black !important;
    border: 1px solid #28a745 !important;
    border-radius: 10px !important;
}

.stInfo {
    background-color: #cce7ff !important;
    color: black !important;
    border: 1px solid #007bff !important;
    border-radius: 10px !important;
}

.stError {
    background-color: #f8d7da !important;
    color: black !important;
    border: 1px solid #dc3545 !important;
    border-radius: 10px !important;
}

/* Metrics - dark bg, cyan values */
[data-testid="metric-container"] {
    background: rgba(26, 26, 46, 0.9) !important;
    border: 2px solid #00ffff !important;
    border-radius: 15px !important;
    color: white !important;
}

[data-testid="metric-value"] {
    color: #00ffff !important;
    font-size: 2.5rem !important;
}

[data-testid="metric-label"] {
    color: white !important;
}

/* Buttons cyan gradient */
.stButton > button {
    background: linear-gradient(45deg, #00ffff, #0080ff) !important;
    color: white !important;
    border-radius: 25px !important;
    border: none !important;
    font-weight: bold !important;
    font-size: 16px !important;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,255,255,0.4) !important;
}

/* Inputs readable */
.stNumberInput label, .stTextInput label {
    color: white !important;
}

/* Title glow */
h1 {
    color: #00ffff !important;
    text-shadow: 0 0 20px rgba(0,255,255,0.8) !important;
}

/* Avatar */
.header-avatar {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
}

.avatar-img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    box-shadow: 0 4px 20px rgba(0,255,255,0.4);
    border: 3px solid #00ffff;
}

/* Footer */
.footer {
    position: fixed;
    bottom: 10px;
    right: 20px;
    background: rgba(0,0,0,0.8);
    border: 1px solid #90EE90;
    border-radius: 15px;
    color: #90EE90 !important;
    padding: 10px;
    font-weight: bold;
}
</style>

<!-- Avatar -->
<div class="header-avatar">
    <img src="images/avatar.jpg" alt="Avatar" class="avatar-img">
</div>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("🧪 Navigation")
page = st.sidebar.radio("Select Feature:", [
    "🏠 Home",
    "Reynolds Number",
    "Heat Transfer",
    "Pressure Drop", 
    "NTU Method",
    "Chemical Formulas",
    "Explain Concepts",
    "💬 General Chat"
])

# Main title
st.title("🧪 Chemical Engineering Assistant Bot")
st.markdown("---")

if page == "🏠 Home":
    st.header("Welcome to ChemEngBot! ✨")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Available Features:")
        st.markdown("""
        1. **Reynolds Number** - Flow type calculator
        2. **Heat Transfer** - Q = U A ΔT calculator
        3. **Pressure Drop** - Pipe pressure loss
        4. **NTU Method** - Heat exchanger effectiveness
        5. **Chemical Formulas** - Key equations
        6. **Explain Concepts** - Engineering terms
        7. **General Chat** - Ask anything!
        """)
    
    with col2:
        st.subheader("🚀 Quick Start:")
        st.markdown("""
        - Select feature from sidebar 🧪
        - Enter parameters 
        - Get instant results with explanations
        - Professional chemical engineering calculations
        
        **Ready?** Choose sidebar option!
        """)

elif page == "Reynolds Number":
    st.header("🔄 Reynolds Number Calculator")
    st.markdown("**Formula: Re = ρvd/μ**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        rho = st.number_input("Density ρ (kg/m³)", min_value=0.1, value=1000.0)
        v = st.number_input("Velocity v (m/s)", min_value=0.1, value=2.0)
    
    with col2:
        d = st.number_input("Diameter d (m)", min_value=0.001, value=0.1)
        mu = st.number_input("Viscosity μ (Pa·s)", min_value=0.0001, value=0.001)
    
    if st.button("Calculate Re", key="reynolds"):
        Re = bot.calculate_reynolds(rho, v, d, mu)
        flow = "Laminar" if Re < 2000 else "Transitional" if Re < 4000 else "Turbulent"
        
        st.success("✅ Success!")
        col1, col2 = st.columns(2)
        col1.metric("Re", f"{Re:.0f}")
        col2.metric("Flow", flow)
        st.info(f"**Re = {Re:.0f} → {flow} flow**")

elif page == "Heat Transfer":
    st.header("🔥 Heat Transfer Q = U A ΔT")
    col1, col2 = st.columns(2)
    
    with col1:
        u = st.number_input("U (W/m²K)", value=100.0)
        a = st.number_input("Area A (m²)", value=10.0)
    
    delta_t = st.number_input("ΔT (K/°C)", value=50.0)
    
    if st.button("Calculate Q"):
        Q = bot.calculate_heat_transfer(u, a, delta_t)
        st.success("✅ Success!")
        st.metric("Heat Rate Q", f"{Q:.0f} W")
        st.info(f"**Q = {u} × {a} × {delta_t} = {Q:.0f} W**")

# ... rest of pages similar with clear emojis and simple structure

# Footer
st.markdown("""
<div class="footer">
    Made with ❤️ by Zunair | ChemEngBot v1.0
</div>
""", unsafe_allow_html=True)
