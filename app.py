from flask import Flask, request, jsonify
from flask.helpers import send_file
from markupsafe import escape
import random

app = Flask(__name__, static_url_path='/', static_folder='frontend')

# Define a global variable
random_number = random.randint(1, 100)

@app.route("/")
def indexPage():
     return send_file("frontend/index.html")

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route("/gues")
def sum_even():
    global random_number
    # flask parameters with type and default
    n = request.args.get('n', default=1, type=int)
    # logic
    if n < random_number:
        result = f"{n} is to low"
    elif n > random_number:
        result = f"{n} is to high"
    else:
        result = f"{n} is your number"
    # return result as json
    return jsonify(result=result)

@app.route("/change")
def change():
    global random_number
    random_number = random.randint(1, 100)
    return

@app.route("/ping")
def hello_world():
    return "<p>Hello, World!</p>"