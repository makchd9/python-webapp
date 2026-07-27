from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    resume = {
        "name": "Daksh Jigar Shah",
        "title": "Computer Science Engineering Student",
        "email": "dakshjigarshah9@gmail.com",
        "phone": "+91 96641 99999",
        "location": "Mumbai, India",
        "linkedin": "#",
        "github": "#"
    }
    return render_template("index.html", resume=resume)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
