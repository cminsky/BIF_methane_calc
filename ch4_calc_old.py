import streamlit as st
import numpy as np

BIF_mass = st.slider(label='BIF mass (1e20 g)',
                     min_value=7.3,max_value=10.)
    # spreadsheet calculation from Bekker et al 2010

Fe_wt = st.slider(label='Fe wt %',min_value=0.2,max_value=0.4)
    # Klein et al. 2005

Fe_C_ratio = st.number_input(label='Fe to C ratio',value=12)
    # The equation from Thibon et al.

CH4_percent = st.slider(label='Portion of BIF formed with CH4 production',
                        min_value=0.,max_value=1.,value=1.)

Fe_mm = 56 # g/mol
NA = 1.87e20 # moles air in the atmosphere
    # Charlotte says just trust me bro
    # 1 atm times Earth surface area

atmos_pressure = st.slider(label='Atmospheric pressure relative to modern',
                           min_value=0.,max_value=1.1,value=0.5)
    # from Catling et al. 2020

# mass of Fe
# currently simplified to just Fe in general
Fe_mass = Fe_wt*BIF_mass
"Fe (1e20 g)",Fe_mass

# moles of Fe
Fe_moles = Fe_mass*1e20/Fe_mm
"Fe (1e18 mol)",Fe_moles/1e18

# moles of Fe related to CH4
Fe_moles_CH4 = Fe_moles*CH4_percent
"Fe (1e18 mol) formed with CH4 production",Fe_moles_CH4/1e18

# moles of CH4
CH4_moles = Fe_moles_CH4/Fe_C_ratio
"CH4 (1e18 mol)",CH4_moles/1e18

# Archean atmosphere air moles
air_moles = NA*atmos_pressure
"1e18 moles air in atmosphere",air_moles/1e18

# ppm CH4
CH4_ppm = CH4_moles/air_moles*1e6
"[CH4] (ppm)",CH4_ppm

# baseline Archean methane
# 1e2 to 1e4 times modern (Catling et al. Archean atmosphere)
# modern is ~1ppm (Google)
"baseline Archean [CH4] = 100-10,000 ppm"

"we got min 1000 ppm max 50,000 ppm"