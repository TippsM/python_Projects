#Lab #2 - Weather and Air Quality Web App using Streamlit and AirVisual API

import streamlit as st
import requests
import main_functions

my_key = main_functions.read_from_file("api_keys.json")
IQair_api_key = my_key["IQ_air_key"]


st.title("Weather and Air Quality Web App")
st.header("Streamlit and AirVisual API")


@st.cache_data
def map_creator(latitude, longitude):
    from streamlit_folium import folium_static
    import folium

    # center on the station
    m = folium.Map(location=[latitude, longitude], zoom_start=10)

    # add marker for the station
    folium.Marker([latitude, longitude], popup="Station", tooltip="Station").add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)


@st.cache_data
def generate_list_of_countries():
    countries_url = f"https://api.airvisual.com/v2/countries?key={IQair_api_key}"
    countries_dictionary = requests.get(countries_url).json()
    #st.write(countries_dictionary)
    return countries_dictionary


@st.cache_data
def generate_list_of_states(country_selected):
    states_url = f"https://api.airvisual.com/v2/states?country={country_selected}&key={IQair_api_key}"
    states_dict = requests.get(states_url).json()
    #st.write(states_dict)
    return states_dict


@st.cache_data
def generate_list_of_cities(state_selected, country_selected):
    cities_url = f"https://api.airvisual.com/v2/cities?state={state_selected}&country={country_selected}&key={IQair_api_key}"
    cities_dict = requests.get(cities_url).json()
    #st.write(cities_dict)
    return cities_dict

#---------------------------------------------------------------------

st.sidebar.title("Choose a category")
category_option = st.sidebar.selectbox("Choose a category", options= ["",
    "By City, State, and Country", "By Nearest City (IP Address)", "By Latitude and Longitude"])


if category_option == "By City, State, and Country":
    countries_dict = generate_list_of_countries()
    if countries_dict["status"] == "success":
        countries_list = []
        for i in countries_dict["data"]:
            countries_list.append(i["country"])
        countries_list.insert(0, "")

        country_selected = st.selectbox("Select a country", options=
        countries_list)

        if country_selected:
            states_dictionary = generate_list_of_states(country_selected)
            state_selected = ""

            if states_dictionary["status"] == "success":
                states_list = []
                for i in states_dictionary["data"]:
                    states_list.append(i["state"])
                states_list.insert(0, "")

                state_selected = st.selectbox("Select a state", options=
                states_list)
            else:
                st.error("No data available for this location.")

            # ---------------------------------------------------------------------

            if state_selected:
                 cities_dictionary = generate_list_of_cities(state_selected, country_selected)
                 cities_list = ""
                 if cities_dictionary["status"] == "success":
                     cities_list = []
                     for i in cities_dictionary["data"]:
                         cities_list.append(i["city"])
                     cities_list.insert(0, "")
                 else:
                     st.warning("No data available for this location.")

                 city_selected = st.selectbox("Select a City", options=
                 cities_list)

                 # ---------------------------------------------------------------------

                 if city_selected:

                    aqi_data_url = (f"https://api.airvisual.com/v2/city?city={city_selected}"
                                    f"&state={state_selected}&country={country_selected}&key={IQair_api_key}")
                    aqi_data_dict = requests.get(aqi_data_url).json()

                    if aqi_data_dict["status"] == "success":

                        # ---------------------------------------------------------------------

                        city_data = aqi_data_dict["data"]
                        city_location = city_data["location"]
                        current_aqi_data = city_data["current"]

                        aqi_data = current_aqi_data["weather"]
                        aqi_data_pollution = current_aqi_data["pollution"]


                        longitude = city_location["coordinates"][0]
                        latitude = city_location["coordinates"][1]

                        celsius_city_temp = aqi_data['tp']
                        fahrenheit_city_temp  = (celsius_city_temp * 9/5) + 32

                        time_stamp = aqi_data['ts']
                        current_date = ""
                        for i in range(10):
                            current_date += time_stamp[i]

                        # ---------------------------------------------------------------------

                        map_creator(latitude, longitude)
                        st.caption(f":green[Today is {current_date}.]")
                        st.info(f"Temperature in {city_selected} is "
                                f"{celsius_city_temp}\u00b0C /{fahrenheit_city_temp:.2f}\u00b0F")
                        st.info(f"Humidity in {city_selected} is {aqi_data['hu']}%")

                        st.info(f"The air quality index is currently {aqi_data_pollution['aqius']}")

                        # ---------------------------------------------------------------------

                    else:
                        st.warning("No data available for this location.")
            else:
                st.warning("No stations available, please select another state.")
        else:
            st.warning("No stations available, please select another country.")
    else:
        st.error("Too many requests. Wait for a few minutes before your next API call.")

elif category_option == "By Nearest City (IP Address)":
    url = f"https://api.airvisual.com/v2/nearest_city?key={IQair_api_key}"
    aqi_data_dict = requests.get(url).json()

    if aqi_data_dict["status"] == "success":

        # ---------------------------------------------------------------------

        city_data = aqi_data_dict["data"]
        city_location = city_data["location"]
        current_aqi_data = city_data["current"]

        aqi_data = current_aqi_data["weather"]
        aqi_data_pollution = current_aqi_data["pollution"]

        longitude = city_location["coordinates"][0]
        latitude = city_location["coordinates"][1]

        celsius_city_temp = aqi_data['tp']
        fahrenheit_city_temp = (celsius_city_temp * 9 / 5) + 32

        time_stamp = aqi_data['ts']
        current_date = ""

        for i in range(10):
            current_date += time_stamp[i]

        # ---------------------------------------------------------------------

        map_creator(latitude, longitude)
        st.caption(f":green[Today is {current_date}.]")

        st.info(f"Temperature in nearest city is "
                f"{celsius_city_temp}\u00b0C /{fahrenheit_city_temp:.2f}\u00b0F")
        st.info(f"Humidity is {aqi_data['hu']}%")

        st.info(f"The air quality index is currently {aqi_data_pollution['aqius']}")

        # ---------------------------------------------------------------------

    else:
        st.warning("No data available for this location.")

elif category_option == "By Latitude and Longitude":
    # TODO: Add two text input boxes for the user to enter the latitude and longitude information
    latitude = st.text_input("Enter latitude, e.g. -21.2404955341995576")
    longitude = st.text_input("Enter longitude, e.g. -44.99782911715176")

    # ---------------------------------------------------------------------

    if latitude and longitude:
        url = f"https://api.airvisual.com/v2/nearest_city?lat={latitude}&lon={longitude}&key={IQair_api_key}"
        aqi_data_dict = requests.get(url).json()

        if aqi_data_dict["status"] == "success":

            # ---------------------------------------------------------------------

            city_data = aqi_data_dict["data"]
            city_location = city_data["location"]

            current_aqi_data = city_data["current"]

            aqi_data_pollution = current_aqi_data["pollution"]
            aqi_data = current_aqi_data["weather"]

            longitude = city_location["coordinates"][0]
            latitude = city_location["coordinates"][1]

            celsius_city_temp = aqi_data['tp']
            fahrenheit_city_temp = (celsius_city_temp * 9 / 5) + 32

            time_stamp = aqi_data['ts']
            current_date = ""

            for i in range(10):
                current_date += time_stamp[i]

            # ---------------------------------------------------------------------

            map_creator(latitude, longitude)
            st.caption(f":green[Today is {current_date}.]")

            st.info(f"Temperature in nearest city is "
                    f"{celsius_city_temp}\u00b0C /{fahrenheit_city_temp:.2f}\u00b0F")
            st.info(f"Humidity is {aqi_data['hu']}%")

            st.info(f"The air quality index is currently {aqi_data_pollution['aqius']}")

        # TODO: Display the weather and air quality data as shown in the video and description of the assignment

        else:
            st.warning("No data available for this location.")

            # ---------------------------------------------------------------------
