import streamlit as st
import ad_model
import htc_model
import power_model

st.set_page_config(page_title="AD-HTC Plant Designer", layout="wide")

st.title("⚡ Integrated AD-HTC Power Plant Simulator")
st.markdown("---")

# SIDEBAR INPUTS
st.sidebar.header("User Input Parameters")
feed_rate = st.sidebar.slider("Feedstock Rate (kg/day)", 100, 5000, 1000)
ad_yield = st.sidebar.number_input("Biogas Yield (m3/kg)", value=0.6)
digestate_ref = st.sidebar.number_input("Digestate Ratio", value=0.4)
htc_yield_ref = st.sidebar.number_input("Hydrochar Yield", value=0.6)

# CALCULATIONS
if st.button("Simulate Plant Performance"):
    # 1. AD Process [cite: 286]
    biogas, digestate = ad_model.anaerobic_digestion(feed_rate, ad_yield, digestate_ref)
    
    # 2. HTC Process [cite: 286]
    hydrochar = htc_model.htc_process(digestate, htc_yield_ref)
    
    # 3. Power Generation [cite: 286]
    b_elec, h_elec = power_model.calculate_power(biogas, hydrochar)
    total_elec = b_elec + h_elec # [cite: 285]

    # DISPLAY RESULTS
    col1, col2, col3 = st.columns(3)
    col1.metric("Biogas Produced", f"{biogas:,.2f} m³/day")
    col2.metric("Hydrochar Produced", f"{hydrochar:,.2f} kg/day")
    col3.metric("Total Electricity", f"{total_elec:,.2f} MJ/day")
    
    st.success(f"The plant is currently generating {total_elec/3.6:,.2f} kWh of energy.")