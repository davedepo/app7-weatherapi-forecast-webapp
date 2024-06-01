import streamlit as st
import plotly.express as px


# set title of the webpage
st.title("Weather Forecast Dashboard")

# add note about the webapp as a caption
st.caption("Welcome to webapp for weather forecast")

# add a text input to enter location
location_input = st.text_input("Enter name of place:",
                               placeholder="Input location ",
                               on_change=None)
st.write("You entered: ", location_input)

# add a slider to choose the options for forecast days
forecast_days = st.slider("Forecast Days",
                          min_value=1,
                          max_value=5,
                          help="Select number of forecast days")

# add a drop-down option to select type of data
option = st.selectbox("Select data to view:",
                      ("Temperature", "Sky"))

# add header to display the output of forecast
st.subheader(f"{option} for the next {forecast_days} days in {location_input}")


# create plotly fig
def get_data(forecast_days):
    date = ["2024-06-02", "2024-06-03", "2024-06-04"]
    temperature = [10, 12, 16]
    temperature = [forecast_days * i for i in temperature]
    return date, temperature


d, t = get_data(forecast_days)
figure = px.line(x=d, y=t, labels={"x": "Date",
                                   "y": "Temp (deg celcius)"})

# display chart
st.plotly_chart(figure)
