# This program defines a simple Flask application to manage posts with CRUD operations.
# It demonstrates the use of Flask routes to handle GET, POST, PUT, PATCH, and DELETE requests.

# Import necessary libraries
from flask import Flask, request, jsonify

# Create a Flask application instance
app = Flask(__name__)

# Example data (simulated)
data = [
    {"id": 1, "title": "Post 1", "body": "This is the body of post 1"},
    {"id": 2, "title": "Post 2", "body": "This is the body of post 2"}
]

# Route for the GET method
@app.route('/posts', methods=['GET'])
def get_posts():
    """
    Get a list of all posts.
    """
    return jsonify(data)

# Route for the POST method
@app.route('/posts', methods=['POST'])
def create_post():
    """
    Create a new post.
    """
    new_post = request.get_json()
    data.append(new_post)
    return jsonify({"message": "Post created successfully"})

# Route for the PUT method (full update)
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    """
    Update an existing post (full update).
    """
    updated_post = request.get_json()
    for post in data:
        if post['id'] == post_id:
            post.update(updated_post)
            return jsonify({"message": f"Post {post_id} updated successfully"})
    return jsonify({"error": "Post not found"}), 404

# Route for the PATCH method (partial update)
@app.route('/posts/<int:post_id>', methods=['PATCH'])
def patch_post(post_id):
    """
    Partially update an existing post.
    """
    updated_data = request.get_json()
    for post in data:
        if post['id'] == post_id:
            post.update(updated_data)
            return jsonify({"message": f"Post {post_id} patched successfully"})
    return jsonify({"error": "Post not found"}), 404

# Route for the DELETE method
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    """
    Delete an existing post.
    """
    global data
    data = [post for post in data if post['id'] != post_id]
    return jsonify({"message": f"Post {post_id} deleted successfully"})

# Run the Flask application
if __name__ == '__main__':
    # Ensure that Flask is installed before running the application
    # You can install Flask by running: pip install flask
    app.run(debug=True)

# Let's go through each CRUD operation step by step, including real examples for each using `curl` for simplicity. Make sure your Flask application is running.

### 1. Retrieve all posts (GET method):

# **URL Path:** `/posts`

# **Command:**
# ```bash
# curl http://127.0.0.1:5000/posts
# ```

# **Example Output:**
# ```json
# [{"id": 1, "title": "Post 1", "body": "This is the body of post 1"},
#  {"id": 2, "title": "Post 2", "body": "This is the body of post 2"}]
# ```

### 2. Create a new post (POST method):

# **URL Path:** `/posts`

# **Command:**
# ```bash
# curl -X POST -H "Content-Type: application/json" -d '{"id": 3, "title": "Post 3", "body": "This is the body of post 3"}' http://127.0.0.1:5000/posts
# ```

# **Example Output:**
# ```json
# {"message": "Post created successfully"}
# ```

### 3. Full update of an existing post (PUT method):

# **URL Path:** `/posts/<int:post_id>` (Replace `<int:post_id>` with the actual post ID, e.g., `/posts/1`)

# **Command:**
# ```bash
# curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Post", "body": "This post has been updated"}' http://127.0.0.1:5000/posts/1
# ```

# **Example Output:**
# ```json
# {"message": "Post 1 updated successfully"}
# ```

### 4. Partial update of an existing post (PATCH method):

# **URL Path:** `/posts/<int:post_id>` (Replace `<int:post_id>` with the actual post ID, e.g., `/posts/2`)

# **Command:**
# ```bash
# curl -X PATCH -H "Content-Type: application/json" -d '{"body": "Partial update to post 2"}' http://127.0.0.1:5000/posts/2
# ```

# **Example Output:**
# ```json
# {"message": "Post 2 patched successfully"}
# ```

### 5. Delete an existing post (DELETE method):

# **URL Path:** `/posts/<int:post_id>` (Replace `<int:post_id>` with the actual post ID, e.g., `/posts/3`)

# **Command:**
# ```bash
# curl -X DELETE http://127.0.0.1:5000/posts/3
# ```

# **Example Output:**
# ```json
# {"message": "Post 3 deleted successfully"}
# ```

# These examples demonstrate how to perform each CRUD operation using `curl` commands. You can replace the values and endpoints based on your specific use case or use tools like Postman for a more graphical interface.
