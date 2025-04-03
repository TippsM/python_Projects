import streamlit as st
import pandas as pd
import plotly.express as px

st.subheader("Water Quality Dashboard")
st.sidebar.subheader("Visualize your Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file "
                                         "(If none is provided, a default dataset is used)")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("10-7-22-mission1.csv")

maps, scatterPlot, linePlot, threeDPlot, tables = st.tabs([
    "Maps", "Scatter Plot", "Line Plot", "3D Plot", "Raw Data & Stats"])
with maps:
    fig1 = px.scatter_mapbox(df,
                             lat = "latitude",
                             lon = "longitude",
                             zoom = 17,
                             mapbox_style="open-street-map",
                             hover_data=df,
                             color="Total Water Column (m)")
    st.plotly_chart(fig1)

with scatterPlot:
    fig2 = px.scatter(df,
                      x="Total Water Column (m)",
                      y = "ODO (mg/L)",
                      color="Temperature (C)",
                      size="pH")
    st.plotly_chart(fig2)

with linePlot:
    col1, col2 = st.columns(2)
    with col1:
        water_parameter = st.selectbox("Select a parameter",
                                       options=["ODO (mg/L)",
                                       "Temperature (C)",
                                                "pH",
                                                "Total Water Column (m)"])
    with col2:
        color_parameter = st.color_picker("Select a color", "#00f900")
        st.write("The chosen color is", color_parameter)

    fig3 = px.line(df,
                   x=df.index,
                   y=water_parameter,
                   title=water_parameter)
    fig3.update_traces(line_color=color_parameter)
    st.plotly_chart(fig3)

with threeDPlot:
    fig4 = px.scatter_3d(df,
                         x = "longitude",
                         y="latitude",
                         z="Total Water Column (m)",
                         color="Total Water Column (m)")
    fig4.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig4)

with tables:
    st.write("Raw Data")
    st.dataframe(df)
    st.write("Descriptive Statistics")
    st.dataframe(df.describe())

    # TODO:  Add a heatmap for correlation between the water quality parameters
    # TODO: Add an expander widget explaining each water quality parameter and its unit
    # TODO: Let the user select which parameter they want for the color of the map or 3d plot
    # TODO: Instead of tabs, is there a better way? Think about usability and efficiency!