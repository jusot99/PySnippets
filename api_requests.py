# Make sure to install the requests library
# You can do this by running: pip install requests

import requests

# URL of the API we will use
url = "https://jsonplaceholder.typicode.com/posts"

# Function to display the response in a readable format
def print_response(response):
    print("Status Code:", response.status_code)
    try:
        print("Response Data:", response.json())
    except ValueError:
        print("Response Data: (non-JSON content)")

# GET Request: Retrieve data
def get_data():
    print("=== GET Request ===")
    response = requests.get(url)
    print_response(response)

# POST Request: Create new data
def create_data():
    print("=== POST Request ===")
    new_post = {"title": "New Post", "body": "This is a new post.", "userId": 1}
    response = requests.post(url, json=new_post)
    print_response(response)

# PUT Request: Update existing data (replace all data)
def update_data():
    print("=== PUT Request ===")
    post_id_to_update = 1
    updated_post = {"title": "Updated Post", "body": "This post has been updated.", "userId": 1}
    update_url = f"{url}/{post_id_to_update}"
    response = requests.put(update_url, json=updated_post)
    print_response(response)

# PATCH Request: Partially update existing data
def patch_data():
    print("=== PATCH Request ===")
    post_id_to_patch = 1
    updated_data = {"body": "This post has been partially updated."}
    patch_url = f"{url}/{post_id_to_patch}"
    response = requests.patch(patch_url, json=updated_data)
    print_response(response)

# DELETE Request: Delete data
def delete_data():
    print("=== DELETE Request ===")
    post_id_to_delete = 1
    delete_url = f"{url}/{post_id_to_delete}"
    response = requests.delete(delete_url)
    print_response(response)

# Execution of functions
get_data()
create_data()
update_data()
patch_data()
delete_data()
