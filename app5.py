import streamlit as st
import requests
import main_functions
import test_mars

my_keys = main_functions.read_from_file("api_keys.json")
my_nasa_api_key = my_keys["nasa_key"]

st.title("NASA API ")
st.subheader("Pictures from Mars")

category = st.selectbox("Choose an API", options=["", "APOD", "Mars Pictures"])

if category == "APOD":
    url_apod = f"http://api.nasa.gov/planetary/apod?api_key={my_nasa_api_key}"
    response = requests.get(url_apod).json()
    st.write(response)
    title = response["title"]
    st.subheader(title)
    st.caption(f"Date: {response['date']}")

    image = response["url"]
    st.image(image)

    explanation = st.checkbox("Check out the explanation")
    if explanation:
        st.write(response["explanation"])

if category == "Mars Pictures":
    st.warning("Under construction")
    url_mars = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={my_nasa_api_key}"
    mars_response = requests.get(url_mars).json()
    select_camera = ['Select a Camera'] + list(test_mars.unique_camera)

    cameras_input = st.selectbox('Choose a Camera', options=select_camera)
    if cameras_input == 'Choose a Camera':
        st.warning("Please Make a Selection")
