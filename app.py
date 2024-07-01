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
    return render_template("pages/landing/home.html")

@app.route("/roomie/form")
def user_form():
    return render_template("pages/roomies/form.html")

@app.route("/roomie/data")
def roomie_data():
    roomies = Roomies()
    data = roomies.get_data()
    return render_template("pages/roomies/information.html", data=data)

@app.route("/roomie/data/<id>")
def get_roomie_by_id(id=None):
    print(id, '=== ID ===')
    roomies = Roomies()
    roomie = roomies.get_roomie_by_id(id)
    if roomie:
        chart_paths = roomies.generate_charts(roomie)
    else:
        chart_paths = {}
    return render_template("pages/roomies/roomie_details.html", roomie=roomie, chart_paths=chart_paths)

if __name__ == "__main__":
    app.run(debug=True)

