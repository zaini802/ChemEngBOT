import streamlit as st
import math

# Set page configuration
st.set_page_config(page_title="ChemEngBot", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        background-color: #f8fafc;
    }
    .stTitle {
        color: #10B981;
        text-align: center;
    }
    h2, h3 {
        color: #059669;
    }
    .stButton > button {
        background-color: #10B981;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

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

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Feature:", [
    "Home",
    "Reynolds Number",
    "Heat Transfer",
    "Pressure Drop",
    "NTU Method",
    "Chemical Formulas",
    "Explain Concepts",
    "General Chat"
])

# Main title
st.title("🧪 Chemical Engineering Assistant Bot")
st.markdown("---")

if page == "Home":
    st.header("Welcome to ChemEngBot!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Available Features:")
        st.write("""
        1. **Reynolds Number** - Calculate flow characteristics
        2. **Heat Transfer** - Compute heat transfer rates
        3. **Pressure Drop** - Calculate pressure losses in pipes
        4. **NTU Method** - Heat exchanger effectiveness
        5. **Chemical Formulas** - View common engineering formulas
        6. **Explain Concepts** - Learn engineering concepts
        7. **General Chat** - Ask general questions
        """)
    
    with col2:
        st.subheader("📚 Quick Guide:")
        st.write("""
        - Select a feature from the sidebar
        - Enter required parameters
        - Get instant calculations and explanations
        - All calculations are accurate and conform to engineering standards
        
        **Ready to start?** Select a feature from the sidebar!
        """)

elif page == "Reynolds Number":
    st.header("Reynolds Number Calculator")
    st.write("Calculate Reynolds number and identify flow type (Laminar, Transitional, or Turbulent)")
    
    st.markdown("**Formula: Re = ρvd/μ**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        rho = st.number_input("Density ρ (kg/m³):", min_value=0.1, value=1000.0, step=10.0)
        v = st.number_input("Velocity v (m/s):", min_value=0.1, value=2.0, step=0.1)
    
    with col2:
        d = st.number_input("Diameter d (m):", min_value=0.001, value=0.1, step=0.01)
        mu = st.number_input("Viscosity μ (Pa·s):", min_value=0.0001, value=0.001, step=0.0001)
    
    if st.button("Calculate Reynolds Number", key="reynolds_calc"):
        try:
            Re = bot.calculate_reynolds(rho, v, d, mu)
            
            if Re < 2000:
                flow_type = "Laminar Flow"
                color = "🟢"
            elif Re < 4000:
                flow_type = "Transitional Flow"
                color = "🟡"
            else:
                flow_type = "Turbulent Flow"
                color = "🔴"
            
            st.success("Calculation Successful!")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Reynolds Number", f"{Re:.2f}")
            with col2:
                st.metric("Flow Type", f"{color} {flow_type}")
            
            st.info(f"**Interpretation:** Re = {Re:.2f} indicates {flow_type.lower()}")
        except Exception as e:
            st.error(f"Error: Please check your inputs. {str(e)}")

elif page == "Heat Transfer":
    st.header("Heat Transfer Calculator")
    st.write("Calculate heat transfer rate using Q = U × A × ΔT")
    
    st.markdown("**Formula: Q = U × A × ΔT**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        u = st.number_input("Heat Transfer Coefficient U (W/m²·K):", min_value=0.1, value=100.0, step=10.0)
        a = st.number_input("Area A (m²):", min_value=0.1, value=10.0, step=0.5)
    
    with col2:
        delta_t = st.number_input("Temperature Difference ΔT (K or °C):", min_value=0.1, value=50.0, step=1.0)
    
    if st.button("Calculate Heat Transfer", key="heat_calc"):
        try:
            Q = bot.calculate_heat_transfer(u, a, delta_t)
            st.success("Calculation Successful!")
            st.metric("Heat Transfer Rate Q", f"{Q:.2f} Watts (W)")
            st.info(f"**Formula Applied:** Q = {u} × {a} × {delta_t} = {Q:.2f} W")
        except Exception as e:
            st.error(f"Error: Please check your inputs. {str(e)}")

elif page == "Pressure Drop":
    st.header("Pressure Drop Calculator")
    st.write("Calculate pressure drop in pipes using: ΔP = f × (L/D) × (ρv²/2)")
    
    st.markdown("**Formula: ΔP = f × (L/D) × (ρv²/2)**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        f = st.number_input("Friction Factor f:", min_value=0.001, value=0.03, step=0.001)
        l = st.number_input("Pipe Length L (m):", min_value=0.1, value=100.0, step=5.0)
        d = st.number_input("Pipe Diameter D (m):", min_value=0.01, value=0.1, step=0.01)
    
    with col2:
        rho = st.number_input("Density ρ (kg/m³):", min_value=0.1, value=1000.0, step=10.0)
        v = st.number_input("Velocity v (m/s):", min_value=0.1, value=2.0, step=0.1)
    
    if st.button("Calculate Pressure Drop", key="pressure_calc"):
        try:
            delta_p = bot.calculate_pressure_drop(f, l, d, rho, v)
            st.success("Calculation Successful!")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Pressure Drop ΔP", f"{delta_p:.2f} Pa")
            with col2:
                st.metric("Pressure Drop (bar)", f"{delta_p/100000:.5f} bar")
        except Exception as e:
            st.error(f"Error: Please check your inputs. {str(e)}")

elif page == "NTU Method":
    st.header("NTU (Number of Transfer Units) Calculator")
    st.write("Calculate NTU and heat exchanger effectiveness")
    
    st.markdown("**Formula: NTU = UA / C_min**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        u = st.number_input("Heat Transfer Coefficient U (W/m²·K):", min_value=0.1, value=100.0, step=10.0, key="ntu_u")
        a = st.number_input("Area A (m²):", min_value=0.1, value=10.0, step=0.5, key="ntu_a")
    
    with col2:
        c_min = st.number_input("Minimum Heat Capacity Rate C_min (W/K):", min_value=0.1, value=500.0, step=10.0)
    
    if st.button("Calculate NTU", key="ntu_calc"):
        try:
            ntu = bot.calculate_ntu(u, a, c_min)
            effectiveness = 1 - math.exp(-ntu)
            
            st.success("Calculation Successful!")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("NTU Value", f"{ntu:.4f}")
            with col2:
                st.metric("Effectiveness", f"{effectiveness:.2%}")
            
            st.info(f"**Interpretation:** NTU = {ntu:.4f} indicates an effectiveness of {effectiveness:.2%} for this heat exchanger configuration.")
        except Exception as e:
            st.error(f"Error: Please check your inputs. {str(e)}")

elif page == "Chemical Formulas":
    st.header("Common Chemical Engineering Formulas")
    
    formulas = {
        "Reynolds Number": "Re = ρvd/μ",
        "Heat Transfer": "Q = UAΔT",
        "Pressure Drop": "ΔP = f × (L/D) × (ρv²/2)",
        "NTU Method": "NTU = UA/C_min",
        "Nusselt Number": "Nu = hL/k",
        "Prandtl Number": "Pr = μCp/k",
        "Grashof Number": "Gr = gβΔTL³ρ²/μ²",
        "Fourier's Law": "q = -k dT/dx"
    }
    
    for name, formula in formulas.items():
        st.markdown(f"**{name}:**")
        st.code(formula, language="latex")

elif page == "Explain Concepts":
    st.header("Learn Engineering Concepts")
    
    concept = st.selectbox(
        "Select a concept to learn about:",
        ["distillation", "heat exchanger", "reactor", "pump", "valve", "npsh", "cavitation", "fouling"]
    )
    
    if concept:
        explanation = bot.explain_concept(concept)
        st.info(explanation)

elif page == "General Chat":
    st.header("General Chat")
    st.write("Ask me anything about chemical engineering!")
    
    user_input = st.text_input("Your question:")
    
    if user_input:
        text = user_input.lower().strip()
        
        if any(word in text for word in ['hi', 'hello', 'hey', 'salam']):
            response = "Assalam-o-Alaikum! How can I assist you with Chemical Engineering today?"
        elif any(word in text for word in ['thanks', 'thank you', 'shukriya']):
            response = "You're welcome! Feel free to ask more questions."
        elif 'help' in text:
            response = "I can help you with: Reynolds Number calculations, Heat Transfer, Pressure Drop, NTU Method, Chemical Formulas, and Engineering Concepts. Select a feature from the sidebar!"
        elif any(word in text for word in ['distillation', 'heat exchanger', 'reactor', 'pump', 'valve', 'npsh', 'cavitation', 'fouling']):
            response = bot.explain_concept(text)
        else:
            response = "I'm not sure about that. Try selecting a specific calculation from the sidebar or ask about: distillation, heat exchanger, reactor, pump, valve, NPSH, cavitation, or fouling."
        
        st.success(response)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h3 style='color: #10B981; margin-bottom: 10px;'>Developed by Zunair Shahzad | UET Lahore</h3>
    <p style='font-size: 18px; color: #059669;'>🔗 <a href='https://github.com/zaini802/ChemEngBOT' target='_blank'>GitHub Repository</a></p>
</div>
""", unsafe_allow_html=True)
