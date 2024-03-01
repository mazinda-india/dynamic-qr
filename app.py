#redirection code
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome!"

@app.route("/redirect-script")
def redirect_user():
    user_agent = request.headers.get('User-Agent')
    if "Android" in user_agent:
        target_url = "https://play.google.com/store/apps/details?id=com.abhey_gupta.MazindaApp"
    elif "iPhone" in user_agent:
        target_url = "https://apps.apple.com/in/app/mazinda-ab-maze-mein-india/id6477349293"
    else:
        target_url = "https://mazinda.com"
    return redirect(target_url)


if __name__ == "__main__":
    app.run(debug=True)

