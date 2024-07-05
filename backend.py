import requests

api_key = "fea4115dedd6eed8f1303fd773a8c061"


def get_data(city_name, forecast_days=None, kind=None):
	api_key = "fea4115dedd6eed8f1303fd773a8c061"
	url = (f"http://api.openweathermap.org/data/2.5/forecast?"
	       f"q={city_name}&"
	       f"appid={api_key}")

	response = requests.get(url)
	data = response.json()

	# check json() output as list
	filtered_data = data["list"]
	print(filtered_data)

	nr_values = 8 * forecast_days
	filtered_data = filtered_data[:nr_values]
	if kind == "Temperature":
		filtered_data = [dict["main"]["temp"] for dict in filtered_data]
	if kind == "Sky":
		filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
	return filtered_data


if __name__ == "__main__":
	print(get_data(city_name="Mumbai", forecast_days=1, kind="Temperature"))
	print(len(get_data(city_name="Mumbai", forecast_days=1, kind="Temperature")))
