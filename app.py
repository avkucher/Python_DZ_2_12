from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from main.views import main_blueprint
from loader.views import load_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"


app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(load_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

