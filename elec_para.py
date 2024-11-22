import streamlit as st

def Elec_Para(V, R, T):
        I = V / R  # Current: I = V / R
        P = I**2 * R  # Power: P = I^2 * R
        H = I**2 * R * T  # Heat: H = I^2 * R * T
        return I, P, H

    

st.title("02341A0259-PS3")
st.markdown("This application is usefull for calculating current through a load,power drawn by the load, and heat energy generated")


col1, col2 = st.columns(2)
with col1:
        with st.container(border=True):
            V = st.number_input("Input voltage (V)", value=100.0)
            R = st.number_input("Load Resistance (R)", value=1000.0)
            T = st.number_input("Time in Hours (T):", value=2.0)
            compute=st.button("Compute")
            

with col2:
        with st.container(border=True):
            if compute:
               I, P, H = Elec_Para(V, R, T)
               st.write(f"Load Current (I): {I:.2f} A")
               st.write(f"Load Power (P): {P:.2f} W")
               st.write(f"Heat Energy (H): {H:.2f} WH")

