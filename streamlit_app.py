import streamlit as st

# Page config
st.set_page_config(
    page_title="ChemEngBot - Chemical Engineering Assistant",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better design
st.markdown("""
    <style>
    /* Main header style */
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Card style */
    .card {
        background-color: #f8f9fa;
        padding: 1.2rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        border-left: 4px solid #4CAF50;
        transition: transform 0.2s;
    }
    
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a3c6e 0%, #0e2a4f 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }
    
    /* Radio button styling */
    [data-testid="stSidebar"] .stRadio div {
        color: white !important;
    }
    
    /* Button styling */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1rem;
        padding: 0.5rem 1rem;
        transition: all 0.3s;
    }
    
    .stButton button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    
    /* Success/Info boxes */
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 2px solid #4CAF50;
        background: linear-gradient(135deg, #1a3c6e 0%, #0e2a4f 100%);
        border-radius: 10px;
    }
    
    .footer-name {
        font-size: 1.8rem !important;
        font-weight: bold !important;
        color: #4CAF50 !important;
        margin-bottom: 0.3rem !important;
    }
    
    .footer-university {
        font-size: 1.2rem !important;
        color: #ccc !important;
    }
    
    .footer-credit {
        font-size: 1rem !important;
        color: #aaa !important;
        margin-top: 0.5rem !important;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        font-size: 1.2rem;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/chemical-plant.png", width=80)
    st.markdown("# 🧪 ChemEngBot")
    st.markdown("---")
    
    # Navigation
    feature = st.radio(
        "📌 **SELECT FEATURE**",
        [
            "🏠 HOME",
            "📊 REYNOLDS NUMBER",
            "🔥 HEAT TRANSFER",
            "📉 PRESSURE DROP",
            "📐 NTU METHOD",
            "📚 FORMULAS",
            "💡 CONCEPTS"
        ],
        index=0
    )
    
    st.markdown("---")
    
    # 👇 YAHAN AAPKA NAAM BARA AUR BOLD DIKHEGA
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <hr style="border-color: #4CAF50;">
        <p style="font-size: 1.5rem; font-weight: bold; color: #4CAF50; margin: 0.5rem 0;">👨‍🔧 ZUNAIR SHAHZAD</p>
        <p style="font-size: 1rem; color: #ccc; margin: 0;">🎓 Chemical Engineering</p>
        <p style="font-size: 1.1rem; color: #4CAF50; font-weight: bold; margin: 0;">UET LAHORE</p>
        <hr style="border-color: #4CAF50;">
    </div>
    """, unsafe_allow_html=True)

# Main content
if feature == "🏠 HOME":
    # Hero section
    st.markdown('<p class="main-header">🧪 Chemical Engineering Assistant Bot</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your AI-Powered Companion for Chemical Engineering Calculations</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Welcome message
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 👋 Welcome to ChemEngBot!
        
        Your personal **Chemical Engineering Assistant** that helps you with:
        
        | ✅ | Feature | Description |
        |---|---|---|
        | 📊 | **Reynolds Number** | Calculate flow characteristics (Laminar/Turbulent) |
        | 🔥 | **Heat Transfer** | Compute heat transfer rates using Q = UAΔT |
        | 📉 | **Pressure Drop** | Calculate pressure losses in pipes |
        | 📐 | **NTU Method** | Heat exchanger effectiveness calculation |
        | 📚 | **Formulas** | View common engineering formulas |
        | 💡 | **Concepts** | Learn engineering concepts |
        
        **Select any feature from the sidebar to get started!**
        """)
    with col2:
        st.image("https://img.icons8.com/color/200/chemical-plant.png")
    
    st.markdown("---")
    
    # Quick stats
    st.subheader("📈 Quick Reference Formulas")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Reynolds Number", "Re = ρvd/μ")
    with col2:
        st.metric("Heat Transfer", "Q = UAΔT")
    with col3:
        st.metric("Pressure Drop", "ΔP = f(L/D)(ρv²/2)")
    with col4:
        st.metric("NTU", "NTU = UA/C_min")

elif feature == "📊 REYNOLDS NUMBER":
    st.header("📊 Reynolds Number Calculator")
    st.markdown("**Formula:** Re = ρvd/μ")
    st.info("💡 Reynolds Number determines flow type: **Laminar** (<2000), **Transitional** (2000-4000), **Turbulent** (>4000)")
    
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("📊 Density ρ (kg/m³):", value=1000.0, step=10.0, format="%.2f")
        v = st.number_input("💨 Velocity v (m/s):", value=1.0, step=0.1, format="%.2f")
    with col2:
        d = st.number_input("📏 Diameter d (m):", value=0.05, step=0.01, format="%.3f")
        mu = st.number_input("💧 Viscosity μ (Pa·s):", value=0.001, step=0.0001, format="%.4f")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔬 Calculate Reynolds Number", type="primary", use_container_width=True):
            if mu > 0:
                Re = (rho * v * d) / mu
                st.success(f"### ✅ Reynolds Number = **{Re:,.2f}**")
                
                if Re < 2000:
                    st.info("🟢 **Flow Type:** Laminar Flow (Smooth, steady)")
                elif Re < 4000:
                    st.warning("🟡 **Flow Type:** Transitional Flow (Unstable)")
                else:
                    st.error("🔴 **Flow Type:** Turbulent Flow (Chaotic, mixing)")
            else:
                st.error("❌ Viscosity must be greater than 0!")

elif feature == "🔥 HEAT TRANSFER":
    st.header("🔥 Heat Transfer Calculator")
    st.markdown("**Formula:** Q = U × A × ΔT")
    st.info("💡 Heat transfer rate is measured in **Watts (W)** or **kilowatts (kW)**")
    
    col1, col2 = st.columns(2)
    with col1:
        U = st.number_input("🔧 U (W/m²·K):", value=500.0, step=50.0)
        A = st.number_input("📐 Area A (m²):", value=10.0, step=1.0)
    with col2:
        dT = st.number_input("🌡️ ΔT (K or °C):", value=50.0, step=5.0)
    
    if st.button("🔥 Calculate Heat Transfer", type="primary"):
        Q = U * A * dT
        st.success(f"### ✅ Heat Transfer Rate = **{Q:,.2f} W**")
        st.info(f"#### 📊 = {Q/1000:.2f} kW")
        import math

elif feature == "📉 PRESSURE DROP":
    st.header("📉 Pressure Drop Calculator")
    st.markdown("**Formula:** ΔP = f × (L/D) × (ρv²/2)")
    st.info("💡 Darcy-Weisbach equation for pipe pressure loss")
    
    col1, col2 = st.columns(2)
    with col1:
        f = st.number_input("Friction factor f:", value=0.02, step=0.001, format="%.4f")
        L = st.number_input("Pipe length L (m):", value=100.0, step=10.0)
    with col2:
        d = st.number_input("Diameter D (m):", value=0.1, step=0.01)
        rho = st.number_input("Density ρ (kg/m³):", value=1000.0, step=100.0)
        v = st.number_input("Velocity v (m/s):", value=2.0, step=0.1)
    
    if st.button("Calculate ΔP", type="primary"):
        delta_P = f * (L / d) * (rho * v**2 / 2)
        st.success(f"### ✅ Pressure Drop = **{delta_P:,.2f} Pa**")
        st.metric("ΔP", f"{delta_P/1000:.2f} kPa")
        st.info(f"**Full calc:** {f} × ({L}/{d}) × ({rho}×{v}²/2)")

elif feature == "📐 NTU METHOD":
    st.header("📐 NTU Method Calculator")
    st.markdown("**Formula:** NTU = UA / C_min")
    st.info("💡 Number of Transfer Units for heat exchangers")
    
    col1, col2 = st.columns(2)
    with col1:
        U = st.number_input("Overall HTC U (W/m²·K):", value=500.0, step=50.0)
        A = st.number_input("Area A (m²):", value=10.0, step=1.0)
    with col2:
        C_min = st.number_input("C_min (W/K):", value=1000.0, step=100.0)
    
    if st.button("Calculate NTU", type="primary"):
        NTU = (U * A) / C_min
        effectiveness = 1 - math.exp(-NTU)  # Counterflow simple case
        st.success(f"### ✅ NTU = **{NTU:.2f}**")
        col1.metric1, col2 = st.columns(2)
        col1.metric("NTU", f"{NTU:.2f}")
        col2.metric("Effectiveness", f"{effectiveness:.1%}")
        st.info("Effectiveness (simple counterflow): 1 - e^(-NTU)")

elif feature == "📚 FORMULAS":
    st.header("📚 Chemical Engineering Formulas")
    st.info("Common equations for quick reference")
    
    st.markdown("""
    | Formula | Description | Equation |
    |---------|-------------|----------|
    | Reynolds Number | Flow regime | Re = ρvd/μ |
    | Heat Transfer | Rate | Q = UAΔT |
    | Pressure Drop | Darcy | ΔP = f(L/D)(ρv²/2) |
    | NTU | Heat exchanger | NTU = UA/C_min |
    | Nusselt | Convection | Nu = hL/k |
    | Prandtl | Fluid prop | Pr = μCp/k |
    | Fourier | Conduction | q = -k∇T |
    | Bernoulli | Energy | P/ρg + v²/2g + z = const |
    """)

elif feature == "💡 CONCEPTS":
    st.header("💡 Engineering Concepts")
    st.info("Ask about key chemical engineering terms")
    
    concept = st.text_input("Enter concept (distillation, heat exchanger, etc.):")
    
    explanations = {
        'distillation': "Distillation: Separation by boiling point. Vapor rises, liquid falls. Used in oil refining.",
        'heat exchanger': "Heat Exchanger: Transfers heat between fluids without mixing. Types: shell-tube, plate.",
        'reactor': "Reactor: Where reactions happen. CSTR, PFR, Batch types.",
        'pump': "Pump: Moves fluids. Centrifugal (high flow), positive displacement.",
        'valve': "Valve: Controls flow. Gate, globe, ball, check valves.",
        'npsh': "NPSH: Net Positive Suction Head - prevents pump cavitation.",
        'cavitation': "Cavitation: Bubbles form from low pressure, damage equipment.",
        'fouling': "Fouling: Deposits reduce heat transfer efficiency."
    }
    
    if st.button("Explain Concept") and concept:
        text_lower = concept.lower()
        explanation = next((v for k, v in explanations.items() if k in text_lower), "No explanation found. Try: distillation, heat exchanger, reactor, pump, valve, npsh, cavitation, fouling")
        st.success(f"**{concept.title()}:** {explanation}")

# 👇 YEH BADA FOOTER HAI — POORE APP KE NICHE DIKHEGA
st.markdown("---")
st.markdown("""
<div class="footer">
    <p class="footer-name">👨‍🔧 ZUNAIR SHAHZAD</p>
    <p class="footer-university">🎓 Chemical Engineering | UET LAHORE</p>
    <p class="footer-credit">🚀 ChemEngBot — Your Chemical Engineering Assistant</p>
    <p class="footer-credit">© 2024 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)