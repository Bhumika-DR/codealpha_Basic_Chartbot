from flask import Flask, render_template, request
from chatbot_logic import get_bot_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    user_input = ""
    bot_response = ""
    
    if request.method == "POST":
        user_input = request.form["message"]
        bot_response = get_bot_response(user_input)
    
    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
