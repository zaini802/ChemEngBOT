import streamlit as st

# Streamlit gallery template - PERFECT working
st.set_page_config(page_title="ChemEngBot", layout="wide")

# Simple sidebar
st.sidebar.title("🧪 ChemEng Tools")
selected = st.sidebar.selectbox("Choose tool:", 
    ["Reynolds Calculator", "Heat Transfer", "Pressure Drop", "NTU", "Formulas"])

# Header
st.title("🧪 ChemEngBot")
st.markdown("---")

if selected == "Reynolds Calculator":
    st.header("Reynolds Number")
    col1, col2 = st.columns(2)
    rho = col1.number_input("Density", value=1000.0)
    v = col1.number_input("Velocity", value=2.0)
    d = col2.number_input("Diameter", value=0.05)
    mu = col2.number_input("Viscosity", value=0.001)
    
    if st.button("Calculate"):
        re = (rho * v * d) / mu
        st.success(f"Re = {re:.0f}")
        flow = "Laminar" if re < 2300 else "Turbulent"
        st.balloons()
        col1, col2 = st.columns(2)
        col1.metric("Re", re)
        col2.metric("Flow", flow)

elif selected == "Heat Transfer":
    st.header("Heat Transfer Q = UAΔT")
    u = st.number_input("U", value=500.0)
    a = st.number_input("Area", value=10.0)
    dt = st.number_input("ΔT", value=30.0)
    if st.button("Calculate"):
        q = u * a * dt
        st.metric("Q", q)

# Footer
st.markdown("---")
st.markdown("*ChemEngBot - Professional calculator*")
