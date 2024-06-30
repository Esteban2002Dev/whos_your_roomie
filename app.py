from flask import Flask, render_template
from controllers.roomies import Roomies

app = Flask(__name__)

"""
    To run the app:
        for each terminal> 
            .venv\Scripts\activate
        npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
        python -m flask --app .\app.py run --debug
"""

@app.route("/")
@app.route("/home")
def home():
    return render_template("pages/home.html")

@app.route("/roomie/form")
def user_form():
    print(Roomies.get_data())
    return render_template("pages/form.html")