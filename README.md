![Static Badge](https://img.shields.io/badge/Project_Status-Complete-brightgreen) ![Static Badge](https://img.shields.io/badge/Build-Passing-brightgreen) ![Static Badge](https://img.shields.io/badge/Open_to_Collaboration-Yes-orange)

<h1> Project: Web App - Weather Forecast API </h1>

This web application, built using Streamlit, provides real-time weather forecasts via API services. 

Streamlit handles the creation of user-friendly widgets and visualization of forecast data, 
while an API service fetches the weather data from the backend

<h3> Table of Contents </h3>

- System Details
- Installation
- Usage
- Screenshots
- Features
- Licence
- Authors and acknowledgment

<h3> System Details </h3>

- **Language:** Built with Python 3.12.
- **Development Environment:** Developed using PyCharm IDE.
- **Version Control:** Managed with Git.

<h3> Installation </h3>

* Clone the repository:
    ```bash
    git clone https://github.com/davedepo/app7-weatherapi-forecast-webapp.git
    ```
* Install dependencies: 
    ```bash
    pip install -r requirements.txt
    ```

<h3> Usage </h3>
 
**A. Run the Web App Locally;**

   - This option is ideal for users familiar with Python programs and the Streamlit framework.
      ```
      streamlit run main.py
      ```
OR,

**B. Host the Web App Online (Optional);**

   - For users familiar with Streamlit servers:
     1. You can deploy the program on a Streamlit server and,
     2. Generate a public website URL.

   Refer to the Streamlit documentation for deployment instructions: https://share.streamlit.io/

<h3> Screenshots </h3>
    
- Fyi only, a snippet of weather API call documentation page:

   ![weather forecast API](/app_screenprint/API_call_webpagepng.png?raw=true)


- Web App displayed as localhost - with Temperature or Sky condition Info:

   ![weather forecast webapp](/app_screenprint/plotting_temp.png?raw=true)
   ![weather forecast webapp](/app_screenprint/plotting_sky.png?raw=true)

<h3> Features </h3>

1. **City Input & Forecast Length Slider**: Allow users to input a city name and select the forecast length (e.g., 3 days, 5 days) using a slider.
2. **Temperature Trends**: Display temperature trends over the selected forecast period using a line graph.
3. **Sky Conditions Visualization**: Show sky conditions (clear, clouds, rain, snow) using relevant images based on the forecast data⁴.

And, other potential use-cases that can expand as;

- **Server Deployment & Public URL:** Host your app on a server (e.g., Heroku, AWS) and provide a public URL for easy access by users.
- **Integration with Existing Platforms:** Collaborate with other platforms (e.g., weather websites, blogs) to embed your weather widget as supplemental information on their pages.
- **Premium User:** We can also create a subscription/revenue based model to monetize this webapp - with data privacy and security of any payment system.

<h3> Licence </h3>

This project is licensed under the MIT License.

<h3> Authors and Acknowledgment </h3>

- **Udemy**: For providing a platform to learn.
- **Ardit Sulce** (https://github.com/arditsulceteaching) : Created a code-along learning module for building this app.
- **Python Developers & Community**: Provided extensive documentation and examples to support this learning.
- **OpenAI and Copilot**: For providing support, assistance, and encouragement in this learning journey.
- **PyCharm Team:** Making it easy to learn with all embedded features for beginners.
