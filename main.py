import requests

# Define the endpoint and parameters
url = "https://api.aviationstack.com/v1/flights"
params = {
    "access_key": "b042372742fb35942698bd9f5c97205d",  # Replace with your actual API key
    "limit": 100,
    "offset": 0,
    "callback": "MY_CALLBACK"  # Typically used for JSONP; omit if you don't need it
}

# Make the GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code} - {response.text}")