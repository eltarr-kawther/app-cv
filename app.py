import streamlit as st
from utils import txt, txt2, txt3, txt4
import numpy as np

st.write('''
# Kawtar ELTARR
''')

st.image('./assets/character.png', width=200)

st.markdown('''
## Work Experience
''')

# Data Scientist, La Plateforme.
# Data Scientist, Enovacom
# Data Scientist, BOURBON OFFSHORE SURF.
# Data Scientist, DATA OBSERVER.
# Data Scientist, DATA OBSERVER.

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("Data Scientist at **Enovacom**.")
with col2:
    st.markdown("*(7 months)*")

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("Data Analyst at **Enovacom**.")
with col2:
    st.markdown("*(6 months)*")

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("Data Scientist at **BOURBON OFFSHORE SURF**.")
with col2:
    st.markdown("*(6 months)*")

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("Data Scientist at **DATA OBSERVER**.")
with col2:
    st.markdown("*(4 months)*")

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("Data Scientist at **DATA OBSERVER**.")
with col2:
    st.markdown("*(3 months)*")

st.markdown('''
## Education
''')

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("Master of Science in Artificial Intelligence, **La Plateforme**.")
with col2:
    st.markdown("*(2020 - Today)*")

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("PostGraduate in Artificial Intelligence, **Ecole Centrale Marseille**.")
with col2:
    st.markdown("*(2019 - 2020)*")

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("Master's Degree in Applied Mathematics and Data Science, **Aix-Marseille Université**.")
with col2:
    st.markdown("*(2017 - 2019)*")

col1, col2 = st.columns([6,1])
with col1:
    st.markdown("Bachelor's Degree in Mathematics and Biology, **Aix-Marseille Université**.")
with col2:
    st.markdown("*(2014 - 2017)*")