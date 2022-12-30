"""WSGI server root module file. Basic routing is implemented here"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
async def hello_world():
    """Health-check backend route

    Returns:
        str: server status string
    """
    return "Server is running", 200
