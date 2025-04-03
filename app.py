import streamlit as st
import pandas as pd
import numpy as np
from datetime import time

DATA_DIMENSIONS = (20, 4)
DATA_COLUMNS = ["A","B", "C","D"]

st.title("Plots and Media Files")
st.subheader("Human-Computer Interactions")


basicPlots = st.checkbox("Basic Plots")
if basicPlots:
    df = pd.DataFrame(np.random.rand(*DATA_DIMENSIONS),
                      columns=DATA_COLUMNS)
    st.dataframe(df)

personalInfo = st.checkbox("Personal Info")
if personalInfo:
    p_info = {
        "name": ["Greg", "Matt", "Leo", "David", "Hafsa"],
        "Height": [184, 156, 222, 112, 180],
        "Weight": [110, 890, 681, 751, 911]
    }

    df2 = pd.DataFrame(p_info)
    st.dataframe(df2)
    avg_weight = df2["Weight"].mean()
    st.write(f"The average weight is {avg_weight} kg")

col1, col2 = st.columns(2)
with col1:
    st.image("sedona_usa-1.jpeg", caption="Sedona, USA")
with col2:
    st.video("volcano-1.mp4")
    st.write("Active Volcano")

st.audio("Alla-Turca-1.mp3")

