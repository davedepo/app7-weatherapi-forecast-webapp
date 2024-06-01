import streamlit as st

# set title of the webpage
st.title("Weather Forecast Dashboard")

# add note about the webapp as a caption
st.caption("Welcome to webapp for weather forecast")

# add a text input to enter location
location_input = st.text_input(
	"Enter name of place:",
	placeholder="Input location ",
	on_change=None)
st.write("You entered: ", location_input)

# add a slider to choose the options for forecast days
forecast_days = st.slider(
					"Forecast Days",
					min_value=1,
					max_value=5,
					help="Select number of forecast days")

# add a drop-down option to select type of data
option = st.selectbox(
	"Select data to view:",
	("Temperature", "Sky"))

# add header to display the output of forecast
st.subheader(f"{option} for the next {forecast_days} days in {location_input}")
