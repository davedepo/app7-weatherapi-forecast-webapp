import requests

API_Key = "2e32e6b6390a42c598d103954240206"


def get_data(place, forecast_days, kind):
	url = (f"http://api.weatherapi.com/v1/forecast.json?"
	       f"key={API_Key}&"
	       f"q={place}&"
	       f"days={forecast_days}")
	response = requests.get(url)
	data = response.json()

	if forecast_days == 1:
		if kind == "Temperature":
			temp1 = data['current']['temp_c']
			return temp1
		elif kind == "Sky":
			skycondition1 = data['current']['condition']['text']
			return skycondition1
	else:
		# Initialize an empty list to store the relevant data
		relevant_data = []

		# Iterate from day 1 to forecast_days
		for day in range(1, forecast_days + 1):
			if kind == "Temperature":
				temp = data['forecast']['forecastday'][day - 1]['day']['avgtemp_c']
				relevant_data.append(temp)
			elif kind == "Sky":
				sky_condition = \
					data['forecast']['forecastday'][day - 1]['day']['condition'][
						'text']
				relevant_data.append(sky_condition)

		return relevant_data


if __name__ == "__main__":
	print(get_data(place='Mumbai', forecast_days=5, kind='Sky'))
