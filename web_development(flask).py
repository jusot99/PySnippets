# Web Development (Flask) Guide

# 1. Importing the Flask module
from flask import Flask, render_template, request, redirect, url_for

# 2. Creating a Flask application
app = Flask(__name__, template_folder='templates')

# 3. Defining routes and views

# Route for the home page
@app.route('/')
def home():
    return 'Hello, Flask!'

# Route with dynamic parameter
@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'

# Route with HTML response using render_template
@app.route('/html')
def html_page():
    return render_template('index.html', message='Welcome to Flask!')

# Route with form submission (GET and POST methods)
@app.route('/form', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form['name']
        return f'Form submitted! Hello, {name}!'
    return render_template('form.html')

# Redirecting to another route
@app.route('/redirect')
def redirect_page():
    return redirect(url_for('home'))

# 4. Running the Flask application
if __name__ == '__main__':
    # Use debug=True for development (auto-reload on code changes, detailed error messages)
    app.run(debug=True)

# This program covers the basics of web development using Flask. Here's a breakdown of the sections:

# Importing Modules: Import necessary modules from Flask, including Flask, render_template, request, redirect, and url_for.

# Creating the Flask App: Create a Flask application instance.

# Defining Routes and Views:

# Define routes for different pages using the @app.route decorator.
# Handle dynamic parameters in routes.
# Render HTML pages using render_template.
# Handle form submission with GET and POST methods.
# Redirect to another route using redirect and url_for.
# Running the Flask App: If the script is executed directly (not imported as a module), run the Flask application.

# To run this Flask application, save it in a file (e.g., app.py) and execute it in the terminal or command prompt. Access the specified routes (e.g., http://localhost:5000) in a web browser to interact with the application.

# Make sure to install Flask before running the program: pip install Flask
