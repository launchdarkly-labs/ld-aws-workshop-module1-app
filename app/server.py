from flask import (
Flask,
render_template
  )
import os

PORT = 8080

app = Flask(__name__)
CLIENT_ID = os.environ.get("CLIENT_ID")

@app.route("/")
def root():
  return render_template("main-dashboard.html", client_id=CLIENT_ID)

@app.route("/dashboard")
def dashboard():
  return render_template("main-dashboard.html", client_id=CLIENT_ID)

@app.route("/profile")
def profile():
  return render_template("profile.html")


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=PORT)
