# Web Requests (requests) Guide

import requests

# 1. Making a GET Request

# Specify the URL for the GET request
url_get = 'https://jsonplaceholder.typicode.com/posts/1'

# Send the GET request
response_get = requests.get(url_get)

# Check if the request was successful (status code 200)
if response_get.status_code == 200:
    # Print the content of the response
    print("GET Response:")
    print(response_get.text)
else:
    print(f"GET Request failed with status code: {response_get.status_code}")

# 2. Making a POST Request

# Specify the URL for the POST request
url_post = 'https://jsonplaceholder.typicode.com/posts'

# Data to be sent in the POST request
data_post = {'title': 'foo', 'body': 'bar', 'userId': 1}

# Send the POST request
response_post = requests.post(url_post, data=data_post)

# Check if the request was successful (status code 201 for created resource)
if response_post.status_code == 201:
    # Print the content of the response
    print("\nPOST Response:")
    print(response_post.json())
else:
    print(f"POST Request failed with status code: {response_post.status_code}")

# 3. Handling Query Parameters

# Specify the URL with query parameters
url_with_params = 'https://jsonplaceholder.typicode.com/posts'

# Define query parameters
params = {'userId': 1, 'id': 2}

# Send the GET request with query parameters
response_params = requests.get(url_with_params, params=params)

# Check if the request was successful (status code 200)
if response_params.status_code == 200:
    # Print the content of the response
    print("\nGET Response with Query Parameters:")
    print(response_params.text)
else:
    print(f"GET Request with Query Parameters failed with status code: {response_params.status_code}")

# 4. Handling Headers

# Specify the URL for a request with custom headers
url_with_headers = 'https://jsonplaceholder.typicode.com/posts/1'

# Define custom headers
headers = {'User-Agent': 'my-app/1.0'}

# Send the GET request with custom headers
response_headers = requests.get(url_with_headers, headers=headers)

# Check if the request was successful (status code 200)
if response_headers.status_code == 200:
    # Print the content of the response
    print("\nGET Response with Custom Headers:")
    print(response_headers.text)
else:
    print(f"GET Request with Custom Headers failed with status code: {response_headers.status_code}")

# Note: Ensure you have an active internet connection to execute the web requests.
