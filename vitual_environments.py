# Virtual Environments Guide

# 1. Creating a Virtual Environment

# In the terminal or command prompt, navigate to your project folder and run:
# python -m venv venv

# This command creates a virtual environment named 'venv' in your project folder.

# 2. Activating the Virtual Environment

# On Windows:
# .\venv\Scripts\activate

# On macOS/Linux:
# source venv/bin/activate

# After activation, your terminal prompt should change to indicate that the virtual environment is active.

# 3. Installing Packages in the Virtual Environment

# With the virtual environment active, use pip to install packages:
# pip install package_name

# Example:
# pip install requests

# 4. Deactivating the Virtual Environment

# To deactivate the virtual environment and return to the global Python environment:
# deactivate

# 5. Using a Requirements File

# Create a file named 'requirements.txt' with a list of dependencies:
# Example 'requirements.txt':
"""
requests==2.26.0
beautifulsoup4==4.10.0
"""

# Install dependencies from the requirements file:
# pip install -r requirements.txt

# 6. Checking Installed Packages

# To see a list of installed packages in the virtual environment:
# pip list

# 7. Using Virtual Environments in Scripts

# You can add the shebang line to the top of your Python script to specify the interpreter and activate the virtual environment:

# Example shebang line for Windows:
# #!./venv/Scripts/python.exe

# Example shebang line for macOS/Linux:
# #!/path/to/venv/bin/python

# 8. Creating a Virtual Environment with a Specific Python Version

# If you have multiple Python versions installed, you can create a virtual environment with a specific version:
# python3.8 -m venv venv

# Note: Ensure you have Python and pip installed on your system before creating virtual environments.

# Virtual environments are an essential tool for managing project dependencies and isolating project environments.
