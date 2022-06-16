import streamlit as st
from PIL import Image

with open("./assets/style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

st.write('''# Kawtar ELTARR''')

image = Image.open('./assets/character.png')
st.image(image, width=200)

st.markdown('''---''')

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown('''## Work Experience''')

# Data Scientist, La Plateforme.
# Data Scientist, Enovacom
# Data Scientist, BOURBON OFFSHORE SURF.
# Data Scientist, DATA OBSERVER.
# Data Scientist, DATA OBSERVER.

col1, col2 = st.columns([2,2])
with col1:
    st.markdown("Data Scientist at **Enovacom**.")
with col2:
    st.markdown("*(7 months)*")

col1, col2 = st.columns([2,2])
with col1:
    st.markdown("Data Analyst at **Enovacom**.")
with col2:
    st.markdown("*(6 months)*")

col1, col2 = st.columns([2,2])
with col1:
    st.markdown("Data Scientist at **BOURBON OFFSHORE SURF**.")
with col2:
    st.markdown("*(6 months)*")

col1, col2 = st.columns([2,2])
with col1:
    st.markdown("Data Scientist at **DATA OBSERVER**.")
with col2:
    st.markdown("*(4 months)*")
st.markdown('''
Topic Modelling of TripAdvisor reviews :
- Python (Numpy, Pandas, dfply, Scikitlearn, NLTK, SpaCy, Gensim, timeit, seaborn)
- Temporal Text Mining
- Natural Language Processing
- Latent Dirichlet Allocation
- Perplexity and coherence
- Git
''')

col1, col2 = st.columns([2,2])
with col1:
    st.markdown("Data Scientist at **DATA OBSERVER**.")
with col2:
    st.markdown("*(3 months)*")
st.markdown('''
Topic Modelling and the optimal number of topics :
- R (dplyr, tidyr, purrr, tidytext, stringr, ggplot2, wordcloud2, topicmodels, httr)
- Text Mining
- Topic Modelling
- Latent Dirichlet Allocation
- Perplexity and coherence
- MySQL
- Git
''')

st.markdown('''## Education''')

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