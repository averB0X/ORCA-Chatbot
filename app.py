import json

from flask import Flask, render_template, request, jsonify
from chatbotv2 import predictClass
from chatbotv2 import getResponse

app = Flask(__name__)

# @app.route("/")
# def index_get():
#     return render_template("index.html")

@app.route('/')
def landing_page():
    return render_template ('Landing page.html')

@app.route('/admin-login')
def admin_login_page():
    return render_template ('Admin Login page.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('Dashboard page.html')

@app.route('/chatbot')
def chatbot_page(): return render_template ('Chatbot page.html')

@app.route('/creating-user')
def creating_user_page():
    return render_template('Creating User page.html')

@app.route('/conversation')
def conversation_page():
    return render_template('Conversation page.html')

@app.post("/predict")
def predict():
    msg = request.get_json().get("message")
    ints = predictClass(msg)
    res = getResponse(ints)
    message = {"answer": res}
    return jsonify(message)
        
if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)