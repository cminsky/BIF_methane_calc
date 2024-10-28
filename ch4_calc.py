import streamlit as st
import numpy as np

state = st.radio(label='Set parameters',
                 options=['Min','Mid','Max'],
                 index = 1,
                 horizontal=True)

if state == 'Min':
    d_BIF_mass = 7.3
    d_Fe_wt = 0.2
    d_atmos_pressure = 1.1
elif state == 'Max':
    d_BIF_mass = 10.
    d_Fe_wt = 0.4
    d_atmos_pressure = 0.23
else:
    d_BIF_mass = 8.7
    d_Fe_wt = 0.3
    d_atmos_pressure = 0.5
    

"---"

col1,col2,col3 = st.columns(3)
with col1:
    BIF_mass = st.slider(label='Global BIF mass (1e20 g)',
                        min_value=7.3,max_value=10.,value=d_BIF_mass,
                        help='Minimum from sum of Bekker et al. 2010')
    Fe_wt = st.slider(label='Average BIF Fe content (wt %)',
                      min_value=0.2,max_value=0.4,value=d_Fe_wt,
                      help='Range from Klein et al. 2005')
    
    Fe_mass = Fe_wt*BIF_mass*1e20 # mass of Fe (g)
    Fe_mm = 56 # molar mass of Fe (g/mol)
    Fe_moles = Fe_mass/Fe_mm # moles of Fe

    "BIF Fe: %0.2e g"%Fe_mass,"$\div$ 56 g/mol =","%0.2e mol"%Fe_moles

with col2:
    Fe_C_ratio = st.number_input(label='Stoichiometric Fe\:C ratio',
                                 value=12,
                                 help='Default from Thibon et al. 2019 eq. 13')
    CH4_percent = st.slider(label='Fraction of BIF formed with CH4 production',
                        min_value=0.,max_value=1.,value=1.)

    Fe_moles_CH4 = Fe_moles*CH4_percent

    # moles of CH4
    CH4_moles = Fe_moles_CH4/Fe_C_ratio
    "CH4 produced: %0.2e mol"%CH4_moles

with col3:
    atmos_pressure = st.slider(label='Atmospheric pressure relative to modern',
                            min_value=0.,max_value=1.1,value=d_atmos_pressure,
                            help='Range from Catling et al. 2020')
    NA = 1.87e20 # moles air in the atmosphere
        # Charlotte says just trust me bro (1 atm times Earth surface area)
    
    # Archean atmosphere air moles
    air_moles = NA*atmos_pressure
    "Archean atmos: %0.2e mol"%air_moles

"---"
"**Result:**"
CH4_ppm = CH4_moles/air_moles*1e6
f"[CH4] = {CH4_ppm:,.0f} ppm"

st.caption("Compare to baseline Archean [CH4] estimate: 100-10,000 ppm (Catling et al. 2020)")