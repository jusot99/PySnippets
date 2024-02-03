# JSON Guide

# 1. Importing the json module
import json

# 2. Creating a JSON string from a Python object (serialization)
python_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
json_string = json.dumps(python_dict)
print("JSON String:", json_string)

# 3. Writing JSON to a file
with open('data.json', 'w') as json_file:
    json.dump(python_dict, json_file)

# 4. Reading JSON from a file
with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print("Loaded Data:", loaded_data)

# 5. Parsing a JSON string (deserialization)
json_data = '{"name": "Bob", "age": 30, "city": "San Francisco"}'
parsed_data = json.loads(json_data)
print("Parsed Data:", parsed_data)

# 6. Handling JSON encoding errors
invalid_dict = {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles', 'birthday': datetime.now()}  # datetime object is not serializable

try:
    json.dumps(invalid_dict)
except json.JSONDecodeError as e:
    print(f"Error encoding JSON: {e}")

# Import the datetime library
import datetime

# 7. Custom JSON encoding with default
def custom_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to string
    raise TypeError("Type not serializable")

custom_json = json.dumps(invalid_dict, default=custom_encoder)
print("Custom JSON Encoding:", custom_json)

# 8. Custom JSON encoding with JSONEncoder subclass
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()  # Convert datetime to string
        return super().default(obj)

custom_encoder_json = json.dumps(invalid_dict, cls=CustomJSONEncoder)
print("Custom Encoder JSON:", custom_encoder_json)

# 9. Handling JSON decoding errors
invalid_json_data = '{"name": "David", "age": 40, "city": "Chicago", "birthday": "2023-01-01T12:30:45Z"}'  # Invalid date string

try:
    json.loads(invalid_json_data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

# Note: Ensure you have the required modules installed before running this program.
# Some commands might need to be adapted based on your operating system and environment.
