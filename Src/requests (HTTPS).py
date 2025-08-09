# Basic GET Request
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # e.g., 200
print(response.text)         # Raw content

# GET request with .json()
data = response.json()
print(data["current_user_url"]) # Sample key from Github API

# Query Parameters (GET)
response = requests.get("http://httpbin.org/get", params = {"name": "Hadi"})
print(response.json())

# POST request

response = requests.post("https://httpbin.org/post", data = {"username": "Hadi", "password" : "abc123"})
print(response.json())

# Error Handling
try:
    response = requests.get("https://nothing.com/invalid-url")
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print ("HTTP Error:", e)
    