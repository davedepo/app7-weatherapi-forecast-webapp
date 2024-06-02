import streamlit as st
import plotly.express as px
from backend import get_data

# set title, add location & forecast widgets
st.title("Weather Forecast Dashboard")
st.caption("Welcome to webapp for weather forecast")

location_input = st.text_input("Enter name of place:",
                               placeholder="Input location ",
                               on_change=None)
st.write("You entered: ", location_input)

forecast_days = st.slider("Forecast Days",
                          min_value=1,
                          max_value=5,
                          help="Select number of forecast days")

option = st.selectbox("Select data to view:",
                      ("Temperature", "Sky"))

st.subheader(f"{option} for the next {forecast_days} days in {location_input}")

if location_input:
    # get temperature/sky data
    filtered_data = get_data(location_input, forecast_days)

    if option == "Temperature":
        temperature = [dict["main"]["temp"] for dict in filtered_data]
        #celsius_values = [(f - 32) * 5 / 9 for f in temperature]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # create temperature plot
        figure = px.line(x=dates, y=temperature, labels={
            "x": "Dates", "y": "Temperature (F)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clouds": "images/cloud.png", "Clear": "images/clear.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        # translating the data
        image_paths = [images[condition] for condition in sky_conditions]
        dates = [dict["dt_txt"] for dict in filtered_data]
        st.image(image=image_paths, caption=dates, width=115)
