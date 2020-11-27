from flask import Flask, render_template, request, redirect


app= Flask(__name__)
user = [""]

@app.route("/", methods = ["GET", "POST"])
def home():
    return render_template("home.html")
    


if __name__ == "__main__":
    app.run()