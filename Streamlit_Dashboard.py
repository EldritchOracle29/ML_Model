import requests
import streamlit as st

# Send data to Flask server (POST request)
def send_data_to_flask(data):
    url = "http://127.0.0.1:5000/predict"
    response = requests.post(url, json=data)
    return response.json()

# Display data from Flask server (GET request)
def get_data_from_flask():
    url = "http://127.0.0.1:5000/data"
    response = requests.get(url)
    return response.json()

# Test sending data
if st.button('Send Data'):
    data = {"key": "value"}
    response = send_data_to_flask(data)
    st.write(response)

# Test retrieving data
if st.button('Get Data'):
    data = get_data_from_flask()
    st.write(data)
