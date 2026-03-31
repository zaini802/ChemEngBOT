import re
import math

class ChemEngBot:
    def __init__(self):
        self.name = "ChemEngBot"
        print("=" * 80)
        print(f"{self.name}: Hello! I am your Chemical Engineering Assistant!")
        print(f"{self.name}: I can help with formulas, calculations, and concepts.")
        print(f"{self.name}: Type 'help' to see what I can do. Type 'quit' to exit.")
        print("=" * 80)
        print("\nOPTIONS AND HOW TO USE:")
        print("-" * 80)
        print("\n1. REYNOLDS NUMBER CALCULATION")
        print("   What it does: Calculates Reynolds number and identifies flow type")
        print("   How to use: Type 'reynolds' or 're number'")
        print("   You will need: Density, Velocity, Diameter, Viscosity")
        
        print("\n2. HEAT TRANSFER CALCULATION")
        print("   What it does: Calculates heat transfer rate using Q = U × A × ΔT")
        print("   How to use: Type 'heat transfer' or 'calculate heat'")
        print("   You will need: Heat transfer coefficient U, Area A, Temperature difference ΔT")
        
        print("\n3. PRESSURE DROP CALCULATION")
        print("   What it does: Calculates pressure drop in pipes")
        print("   How to use: Type 'pressure drop'")
        print("   You will need: Friction factor, Pipe length, Pipe diameter, Density, Velocity")
        
        print("\n4. NTU METHOD CALCULATION")
        print("   What it does: Calculates Number of Transfer Units and effectiveness")
        print("   How to use: Type 'ntu'")
        print("   You will need: Heat transfer coefficient U, Area A, Minimum heat capacity rate C_min")
        
        print("\n5. VIEW COMMON FORMULAS")
        print("   What it does: Shows all common chemical engineering formulas")
        print("   How to use: Type 'formula'")
        print("   You will need: Nothing - just view the formulas")
        
        print("\n6. EXPLAIN CONCEPTS")
        print("   What it does: Provides explanations of engineering concepts")
        print("   How to use: Type 'what is [concept]' or 'explain [concept]'")
        print("   Examples: 'what is distillation', 'explain heat exchanger'")
        print("   Available concepts: distillation, heat exchanger, reactor, pump, valve,")
        print("                      npsh, cavitation, fouling")
        
        print("\n" + "=" * 80)
        print("COMMANDS:")
        print("-" * 80)
        print("  'help'    : Repeat this full instruction guide")
        print("  'quit'    : Exit the chatbot")
        print("=" * 80)
        print("\nReady to start! What would you like to do?\n")
    
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
    
    def get_response(self, user_input):
        text = user_input.lower().strip()
        
        # Reynolds number calculation
        if 'reynolds' in text or 're number' in text:
            return self.ask_reynolds()
        
        # Heat transfer calculation
        elif 'heat transfer' in text or 'q =' in text or 'calculate heat' in text:
            return self.ask_heat_transfer()
        
        # Pressure drop
        elif 'pressure drop' in text or 'δp' in text:
            return self.ask_pressure_drop()
        
        # NTU method
        elif 'ntu' in text:
            return self.ask_ntu()
        
        # Formulas
        elif 'formula' in text:
            return self.show_formulas()
        
        # Help
        elif 'help' in text:
            return self.show_help()
        
        # Concepts
        elif 'what is' in text or 'explain' in text:
            return self.explain_concept(text)
        
        # Greeting
        elif any(word in text for word in ['hi', 'hello', 'hey', 'salam']):
            return "Assalam-o-Alaikum! How can I assist you with Chemical Engineering today?"
        
        # Thanks
        elif any(word in text for word in ['thanks', 'thank you', 'shukriya']):
            return "You're welcome! Feel free to ask more questions."
        
        else:
            return self.fallback_response()
    
    def ask_reynolds(self):
        try:
            print("\n--- Reynolds Number Calculation ---")
            rho = float(input("Enter density ρ (kg/m³): "))
            v = float(input("Enter velocity v (m/s): "))
            d = float(input("Enter diameter d (m): "))
            mu = float(input("Enter viscosity μ (Pa·s): "))
            
            Re = self.calculate_reynolds(rho, v, d, mu)
            
            if Re < 2000:
                flow_type = "Laminar Flow"
            elif Re < 4000:
                flow_type = "Transitional Flow"
            else:
                flow_type = "Turbulent Flow"
            
            return f"\nReynolds Number = {Re:.2f}\nFlow Type: {flow_type}"
        except:
            return "Error: Please enter valid numbers."
    
    def ask_heat_transfer(self):
        try:
            print("\n--- Heat Transfer Calculation ---")
            print("Formula: Q = U × A × ΔT")
            u = float(input("Enter overall heat transfer coefficient U (W/m²·K): "))
            a = float(input("Enter area A (m²): "))
            delta_t = float(input("Enter temperature difference ΔT (K or °C): "))
            
            Q = self.calculate_heat_transfer(u, a, delta_t)
            return f"\nHeat Transfer Rate Q = {Q:.2f} Watts (W)"
        except:
            return "Error: Please enter valid numbers."
    
    def ask_pressure_drop(self):
        try:
            print("\n--- Pressure Drop Calculation ---")
            print("Formula: ΔP = f × (L/D) × (ρv²/2)")
            f = float(input("Enter friction factor f: "))
            l = float(input("Enter pipe length L (m): "))
            d = float(input("Enter pipe diameter D (m): "))
            rho = float(input("Enter density ρ (kg/m³): "))
            v = float(input("Enter velocity v (m/s): "))
            
            delta_p = self.calculate_pressure_drop(f, l, d, rho, v)
            return f"\nPressure Drop ΔP = {delta_p:.2f} Pascals (Pa)"
        except:
            return "Error: Please enter valid numbers."
    
    def ask_ntu(self):
        try:
            print("\n--- NTU (Number of Transfer Units) Calculation ---")
            print("Formula: NTU = UA / C_min")
            u = float(input("Enter overall heat transfer coefficient U (W/m²·K): "))
            a = float(input("Enter area A (m²): "))
            c_min = float(input("Enter minimum heat capacity rate C_min (W/K): "))
            
            ntu = self.calculate_ntu(u, a, c_min)
            effectiveness = 1 - math.exp(-ntu)  # For simple case
            
            return f"\nNTU = {ntu:.2f}\nEstimated Effectiveness (for simple case) = {effectiveness:.2%}"
        except:
            return "Error: Please enter valid numbers."
    
    def show_formulas(self):
        return """
Common Chemical Engineering Formulas:

1. **Reynolds Number:** Re = ρvd/μ
2. **Heat Transfer:** Q = UAΔT
3. **Pressure Drop:** ΔP = f × (L/D) × (ρv²/2)
4. **NTU Method:** NTU = UA/C_min
5. **Nusselt Number:** Nu = hL/k
6. **Prandtl Number:** Pr = μCp/k
7. **Grashof Number:** Gr = gβΔTL³ρ²/μ²
8. **Fourier's Law:** q = -k dT/dx

Type the name to learn more!
"""
    
    def show_help(self):
        return """
================================================================================
OPTIONS AND HOW TO USE:
================================================================================

1. REYNOLDS NUMBER CALCULATION
   What it does: Calculates Reynolds number and identifies flow type
   How to use: Type 'reynolds' or 're number'
   You will need: Density, Velocity, Diameter, Viscosity

2. HEAT TRANSFER CALCULATION
   What it does: Calculates heat transfer rate using Q = U × A × ΔT
   How to use: Type 'heat transfer' or 'calculate heat'
   You will need: Heat transfer coefficient U, Area A, Temperature difference ΔT

3. PRESSURE DROP CALCULATION
   What it does: Calculates pressure drop in pipes
   How to use: Type 'pressure drop'
   You will need: Friction factor, Pipe length, Pipe diameter, Density, Velocity

4. NTU METHOD CALCULATION
   What it does: Calculates Number of Transfer Units and effectiveness
   How to use: Type 'ntu'
   You will need: Heat transfer coefficient U, Area A, Minimum heat capacity rate C_min

5. VIEW COMMON FORMULAS
   What it does: Shows all common chemical engineering formulas
   How to use: Type 'formula'
   You will need: Nothing - just view the formulas

6. EXPLAIN CONCEPTS
   What it does: Provides explanations of engineering concepts
   How to use: Type 'what is [concept]' or 'explain [concept]'
   Examples: 'what is distillation', 'explain heat exchanger'
   Available: distillation, heat exchanger, reactor, pump, valve, npsh, cavitation, fouling

================================================================================
COMMANDS:
================================================================================
  'help'  : Show this help guide again
  'quit'  : Exit the chatbot
================================================================================
"""
    
    def explain_concept(self, text):
        if 'distillation' in text:
            return "Distillation: A separation process that uses boiling point differences. Hot vapor rises, cool liquid falls. Used in refineries to separate crude oil into petrol, diesel, etc."
        
        elif 'heat exchanger' in text:
            return "Heat Exchanger: A device that transfers heat between two fluids without mixing them. Types include shell-and-tube, plate, and double-pipe."
        
        elif 'reactor' in text:
            return "Chemical Reactor: Vessel where chemical reactions occur. Types: CSTR (Continuous Stirred Tank), PFR (Plug Flow), and Batch Reactors."
        
        elif 'pump' in text:
            return "Pump: A device that moves fluids by mechanical action. Types: centrifugal, positive displacement, diaphragm pumps."
        
        elif 'valve' in text:
            return "Valve: Controls fluid flow. Types: gate, globe, ball, butterfly, check valves."
        
        elif 'npsh' in text:
            return "NPSH (Net Positive Suction Head): Minimum pressure required at pump suction to avoid cavitation. Critical for pump selection."
        
        elif 'cavitation' in text:
            return "Cavitation: Formation of vapor bubbles in liquid due to low pressure. Damages pumps and valves. Prevented by maintaining adequate NPSH."
        
        elif 'fouling' in text:
            return "Fouling: Deposit buildup on heat exchanger surfaces. Reduces efficiency. Prevented by cleaning and using fouling factors in design."
        
        else:
            return "I can explain: distillation, heat exchanger, reactor, pump, valve, NPSH, cavitation, fouling. Type 'help' for more options."
    
    def fallback_response(self):
        return "I'm not sure about that. Type 'help' to see what I can do, or 'formula' to see common equations."
    
    def chat(self):
        while True:
            user_input = input("\nYou: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(f"\n{self.name}: Goodbye! Keep learning Chemical Engineering!")
                break
            
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")

# Run the bot
if __name__ == "__main__":
    bot = ChemEngBot()
    bot.chat()
