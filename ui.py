# import os
# import streamlit as st
# import requests
# from dotenv import load_dotenv
import os
import streamlit as st
from urllib import request
from urllib.parse import urlencode
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8051))


# Streamlit UI elements
st.title("CLOTHES FOR TODAY'S WEATHER")

question = st.text_input(
    "Which city do you live in?",
    placeholder="Enter your city name here",
)

# if question:
#     url = f"https://{api_host}:{api_port}/"
#     data = {"query": question}

#     response = requests.post(url, json=data)

#     if response.status_code == 200:
#         st.write("### Answer")
#         st.write(response.json())
#     else:
#         st.error(
#             f"Failed to send data to Pathway API. Status code: {response.status_code}"
#         )
if question:
    url = f"https://{api_host}:{api_port}/?{urlencode({'query': question})}"

    st.write("Debugging Info:")
    st.write(f"API URL: {url}")

    try:
        with request.urlopen(url) as response:
            if response.getcode() == 200:
                data = json.loads(response.read().decode("utf-8"))
                st.write("### Answer")
                st.write(data)
            else:
                st.error(
                    f"Failed to send data to Pathway API. Status code: {response.getcode()}"
                )
    except Exception as e:
        st.error(f"Connection Error: {e}")
