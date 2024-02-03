# This program demonstrates different uses of context managers in Python.

# Using a context manager with the 'with' statement
with open('example.txt', 'w') as file:
    file.write("This is a sample text file.\n")
    file.write("It is used to demonstrate context managers in Python.\n")

# Using a custom context manager class
class MyContextManager:
    def __enter__(self):
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

# Using the custom context manager with 'with' statement
with MyContextManager():
    print("Inside the context")

# Using contextlib for a simple context manager
from contextlib import contextmanager

@contextmanager
def simple_context_manager():
    print("Entering the context")
    yield
    print("Exiting the context")

# Using the simple context manager with 'with' statement
with simple_context_manager():
    print("Inside the context")

# Using the 'closing' context manager for resources that need closing
from contextlib import closing
from urllib.request import urlopen
from urllib.error import URLError

url = 'https://www.example.com'

try:
    with closing(urlopen(url)) as response:
        html_content = response.read()
        print("Length of content:", len(html_content))
except URLError as e:
    print(f"Error accessing URL: {e}")

# Using the 'redirect_stdout' context manager for redirecting stdout
from contextlib import redirect_stdout
import io

# Redirect stdout to a variable
output_buffer = io.StringIO()

with redirect_stdout(output_buffer):
    print("This will be captured by the buffer")

# Access the captured output
captured_output = output_buffer.getvalue()
print("\nCaptured output:", captured_output)
