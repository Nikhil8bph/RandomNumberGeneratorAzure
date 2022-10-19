from flask import Flask, render_template, request
import random
list_1_to_100 = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/forward/", methods=['POST','GET'])
def move_forward():
    global list_1_to_100
    forward_message = "The Numbers will be displayed here..."
    if request.method == 'GET':
        list_1_to_100 = list(range(1,101))
    if request.method == 'POST':
        forward_message = random.choice(list_1_to_100)
        list_1_to_100.remove(forward_message)
    return render_template('index.html', forward_message=forward_message, numbers_available = list_1_to_100)

