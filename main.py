from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from vision import list_of_objects

app = Flask(__name__)
# socketio = SocketIO(app)

print(list_of_objects)

# answers = {
#     'Player 1: ' ,
#     'Player 2: '
# }

@app.route("/")
def home():
    return render_template("index.html")

# @socketio.on('connect')
# def connect():
#     emit('after connect', {'data':'Lets play'})

# # Receiving messages from client
# @socketio.on('message')
# def handle_message(message):
#     values[message['who']] = message['data']
#     print('received message: ' + message)
#     # emit('update value', message, broadcast=True)

if __name__ == "__main__":
    app.run(debug=True)