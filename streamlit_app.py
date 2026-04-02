import streamlit as st

# Page config
st.set_page_config(
    page_title="ChemEngBot",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS (optional - for better look)
st.markdown("""
    <style>
    /* Main header */
    .main-header {
        font-size: 2.5rem;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Card style */
    .card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1e3a8a;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/chemical-plant.png", width=80)
    st.title("🧪 ChemEngBot")
    st.markdown("---")
    
    # Navigation
    feature = st.radio(
        "📌 **Select Feature**",
        [
            "🏠 Home",
            "📊 Reynolds Number",
            "🔥 Heat Transfer",
            "📉 Pressure Drop",
            "📚 Formulas",
            "💡 Concepts"
        ],
        index=0
    )
    
    st.markdown("---")
    st.caption("👨‍🔧 Developed by **Zunair Shahzad**")
    st.caption("🎓 UET Lahore")

# Main content area
if feature == "🏠 Home":
    # Hero section
    st.markdown('<p class="main-header">Chemical Engineering Assistant Bot</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Welcome message
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 👋 Welcome to ChemEngBot!
        
        Your personal **Chemical Engineering Assistant** that helps you with:
        
        - ✅ Instant calculations
        - ✅ Formula references
        - ✅ Concept explanations
        
        **Select any feature from the sidebar to get started!**
        """)
    with col2:
        st.image("https://img.icons8.com/color/200/chemical-plant.png")
    
    st.markdown("---")
    
    # Features grid
    st.subheader("📋 Available Features")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 📊 **Reynolds Number**")
            st.write("Calculate flow characteristics (Laminar/Turbulent)")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 📉 **Pressure Drop**")
            st.write("Calculate pressure losses in pipes")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 🔥 **Heat Transfer**")
            st.write("Compute heat transfer rates (Q = UAΔT)")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 📐 **NTU Method**")
            st.write("Heat exchanger effectiveness")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 📚 **Formulas**")
            st.write("View common engineering formulas")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### 💡 **Concepts**")
            st.write("Learn engineering concepts")
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick stats
    st.markdown("---")
    st.subheader("📈 Quick Reference")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Reynolds Number", "Re = ρvd/μ")
    with col2:
        st.metric("Heat Transfer", "Q = UAΔT")
    with col3:
        st.metric("Pressure Drop", "ΔP = f(L/D)(ρv²/2)")
    with col4:
        st.metric("NTU", "NTU = UA/C_min")

elif feature == "📊 Reynolds Number":
    st.header("📊 Reynolds Number Calculator")
    st.markdown("**Formula:** Re = ρvd/μ")
    st.info("Reynolds Number determines flow type: Laminar (<2000), Transitional (2000-4000), Turbulent (>4000)")
    
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Density ρ (kg/m³):", value=1000.0, step=10.0, format="%.2f")
        v = st.number_input("Velocity v (m/s):", value=1.0, step=0.1, format="%.2f")
    with col2:
        d = st.number_input("Diameter d (m):", value=0.05, step=0.01, format="%.3f")
        mu = st.number_input("Viscosity μ (Pa·s):", value=0.001, step=0.0001, format="%.4f")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔬 Calculate Reynolds Number", type="primary", use_container_width=True):
            if mu > 0:
                Re = (rho * v * d) / mu
                st.success(f"### Reynolds Number = **{Re:.2f}**")
                
                if Re < 2000:
                    st.info("🟢 **Flow Type:** Laminar Flow")
                elif Re < 4000:
                    st.warning("🟡 **Flow Type:** Transitional Flow")
                else:
                    st.error("🔴 **Flow Type:** Turbulent Flow")
            else:
                st.error("❌ Viscosity must be greater than 0!")

elif feature == "🔥 Heat Transfer":
    st.header("🔥 Heat Transfer Calculator")
    st.markdown("**Formula:** Q = U × A × ΔT")
    st.info("Heat transfer rate in Watts (W)")
    
    col1, col2 = st.columns(2)
    with col1:
        U = st.number_input("Overall heat transfer coefficient U (W/m²·K):", value=500.0, step=50.0)
        A = st.number_input("Area A (m²):", value=10.0, step=1.0)
    with col2:
        dT = st.number_input("Temperature difference ΔT (K or °C):", value=50.0, step=5.0)
    
    if st.button("🔥 Calculate Heat Transfer", type="primary"):
        Q = U * A * dT
        st.success(f"### Heat Transfer Rate = **{Q:,.2f} W**")
        st.info(f"#### {Q/1000:.2f} kW")

# Add more features as needed...